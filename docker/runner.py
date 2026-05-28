#!/usr/bin/env python3
import json
import os
import subprocess
import sys
import tempfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8787"))
MAX_CODE_BYTES = 80_000


def limit_child():
    try:
        import resource

        resource.setrlimit(resource.RLIMIT_CPU, (4, 4))
        resource.setrlimit(resource.RLIMIT_AS, (256 * 1024 * 1024, 256 * 1024 * 1024))
        resource.setrlimit(resource.RLIMIT_FSIZE, (1024 * 1024, 1024 * 1024))
    except Exception:
        pass


class RunnerHandler(BaseHTTPRequestHandler):
    server_version = "CyberCourseRunner/1.0"

    def _headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.end_headers()

    def do_OPTIONS(self):
        self._headers(204)

    def do_GET(self):
        if self.path != "/health":
            self._headers(404)
            self.wfile.write(json.dumps({"ok": False, "error": "not found"}).encode())
            return
        self._headers(200)
        self.wfile.write(json.dumps({"ok": True}).encode())

    def do_POST(self):
        if self.path != "/run":
            self._headers(404)
            self.wfile.write(json.dumps({"ok": False, "error": "not found"}).encode())
            return

        try:
            size = int(self.headers.get("content-length", "0"))
            if size > MAX_CODE_BYTES:
                raise ValueError("submission too large")
            payload = json.loads(self.rfile.read(size).decode("utf-8"))
            code = str(payload.get("code", ""))
            timeout = min(max(float(payload.get("timeout", 3)), 1.0), 5.0)
        except Exception as exc:
            self._headers(400)
            self.wfile.write(json.dumps({"ok": False, "status": "error", "stderr": str(exc)}).encode())
            return

        with tempfile.TemporaryDirectory(prefix="course-run-") as td:
            path = os.path.join(td, "submission.py")
            with open(path, "w", encoding="utf-8") as f:
                f.write(code)
            try:
                proc = subprocess.run(
                    [sys.executable, "-I", path],
                    cwd=td,
                    env={"PYTHONIOENCODING": "UTF-8"},
                    capture_output=True,
                    text=True,
                    timeout=timeout,
                    preexec_fn=limit_child if os.name == "posix" else None,
                )
                status = "passed" if proc.returncode == 0 else "failed"
                body = {
                    "ok": True,
                    "status": status,
                    "returncode": proc.returncode,
                    "stdout": proc.stdout[-6000:],
                    "stderr": proc.stderr[-6000:],
                }
            except subprocess.TimeoutExpired as exc:
                body = {
                    "ok": True,
                    "status": "timeout",
                    "returncode": None,
                    "stdout": (exc.stdout or "")[-6000:] if isinstance(exc.stdout, str) else "",
                    "stderr": "Timed out. Check for infinite loops or very slow code.",
                }

        self._headers(200)
        self.wfile.write(json.dumps(body).encode("utf-8"))

    def log_message(self, fmt, *args):
        return


if __name__ == "__main__":
    ThreadingHTTPServer((HOST, PORT), RunnerHandler).serve_forever()
