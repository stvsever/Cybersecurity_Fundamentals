<div align="center">
  <h1>The Full Spectrum of Cybersecurity Fundamentals</h1>

  <p>
    <a href="#"><img src="https://img.shields.io/badge/License-MIT-0b7a5e.svg?style=flat-square" alt="MIT Licensed" /></a>
    <a href="#"><img src="https://img.shields.io/badge/Modules-20-0b7a5e.svg?style=flat-square" alt="20 modules" /></a>
    <a href="#"><img src="https://img.shields.io/badge/Diagrams-24_interactive-0b7a5e.svg?style=flat-square" alt="24 interactive diagrams" /></a>
    <a href="#"><img src="https://img.shields.io/badge/Build-none_required-0b7a5e.svg?style=flat-square" alt="No build step" /></a>
  </p>

  <p><b>A free, browser-based cybersecurity course in one HTML file.</b><br>
  Twenty modules from cryptography to governance, every complex mechanism drawn as an
  interactive diagram, plus checked exercises and a scored mock exam.</p>

  <h3>&nbsp;</h3>

  <a href="https://stvsever.github.io/Cybersecurity_Fundamentals/src/index.html">
    <img src="src/assets/open-course.gif" alt="Open the interactive course" width="380" />
  </a>

  <p><sub>
    Runs in the browser, no install, no account.<br>
    Direct link: <a href="https://stvsever.github.io/Cybersecurity_Fundamentals/src/index.html"><b>stvsever.github.io/Cybersecurity_Fundamentals</b></a>
  </sub></p>

  <h3>&nbsp;</h3>

  <a href="https://stvsever.github.io/Cybersecurity_Fundamentals/src/index.html">
    <img src="src/assets/overview.png" alt="The course, reading one module at a time" width="900" />
  </a>

  <hr>

</div>

## Contents

- [Quick Start](#quick-start)
- [What Is Included](#what-is-included)
- [Course Structure](#course-structure)
- [Interactive Features](#interactive-features)
- [Exercises And Mock Exam](#exercises-and-mock-exam)
- [Settings And Local Data](#settings-and-local-data)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Project Structure](#project-structure)
- [Responsible Use](#responsible-use)
- [License](#license)

## Quick Start

### 1. Read the course

There is nothing to build for reading the course.

```bash
open src/index.html          # macOS
xdg-open src/index.html      # Linux
start src/index.html         # Windows
```

You can also open the root `index.html`, which redirects to the course in `src/`.

Progress, visual preferences, settings, exercise drafts, review flags, exam work, and attempt history are saved locally in your browser with `localStorage`.

### 2. Run the Python exercise checker

The Python exercises in pane `02 Exercises` use a local runner for deterministic checks. For Docker, Docker Desktop or the Docker daemon must be running.

```bash
docker build -t cyber-course-runner docker
docker run --rm -p 8787:8787 cyber-course-runner
```

Then open the course, go to `02 Exercises`, choose `Check runtime`, and run the coding checks. The browser sends code only to `http://127.0.0.1:8787/run` on your machine. No LLM grading is used.

Without Docker, run the same checker directly from the repository root. This is the simplest option:

```bash
python3 docker/runner.py
```

Leave that terminal open. The Exercises pane shows the exact command, a copy button, and a live status indicator, and every other exercise type works without the runner. If you moved the runner to another port or host, change the endpoint in Settings under Assessments.

## What Is Included

- 20 curriculum modules with worked code examples and real-world cases in the lessons.
- Module-by-module reading by default, with previous and next navigation above and below each module, plus a full-course mode for reference reading.
- 24 interactive, individually collapsible SVG diagrams built from measured text so labels never collide: UML sequence diagrams for the TLS 1.3 handshake, Kerberos, OpenID Connect with PKCE, DNS resolution, the TCP handshake and port scanning, Tor circuit construction, C2 beaconing, and the CSRF/SSRF/BOLA comparison; architecture diagrams for zero trust, AES-GCM, the Kubernetes control plane, ATT&CK attack paths, agentic AI, and the source-control platform; sequential-parallel pipelines for detection engineering, the software supply chain, and post-quantum migration; plus cycle, swimlane, layer, and encapsulation models.
- Each diagram can be stepped through or played, with a per-step explanation panel.
- A first-visit guided walkthrough that defocuses everything except the highlighted element, with a replay option in Settings.
- Search with all-match highlighting and previous/next navigation.
- A dedicated `02 Exercises` pane with section, format, status, and topic filters across 372 practice items, plus saved review flags and mastery state.
- A dedicated module on version control and secure software delivery: Git integrity and provenance, source-platform threat modelling, protected branches, signed commits, secrets handling, OIDC federation for pipelines, SBOM, VEX, Sigstore, in-toto, and SLSA.
- A separate `03 Mock Exam` pane with sampled attempts, review flags, a question navigator, local attempt history, and 1000-point scoring.
- MITRE ATT&CK Enterprise, Mobile ATT&CK, and ATLAS teaching matrices.
- Refreshed 2026 coverage for ATT&CK v19.2, the OWASP Top 10 for LLM Applications 2026, the OWASP Top 10 for Agentic Applications 2026, NIST CSF 2.0, the NIST Cyber AI Profile draft, post-quantum standards including ML-KEM, ML-DSA, SLH-DSA, and HQC, and the EU Cyber Resilience Act.
- D3FEND countermeasure knowledge-graph structure mapped to ATT&CK-style defensive design.
- Threat intelligence interoperability: STIX 2.1, TAXII 2.1, MISP, OpenCTI, markings, confidence, expiry, and dissemination controls.
- DISARM Red and Blue influence-operation analysis for FIMI, hack-and-leak operations, Doppelganger-style media cloning, amplification, response, and evidence handling.

## Course Structure

| Part | Modules | Focus |
|---|---:|---|
| I. Foundations and the Adversary | 01-02 | Security properties, risk, threat actors, cybercrime economy |
| II. Technical Core and Cloud | 03-07 | Cryptography, IAM, network security, traffic analysis, web application security, cloud, containers |
| III. Offensive Operations | 08-09 | MITRE ATT&CK, Mobile ATT&CK, D3FEND, reconnaissance, exploitation, C2 |
| IV. Defensive Operations and Intelligence | 10-13 | SOC, detection engineering, DFIR, malware, ransomware, botnets, CTI, OSINT, STIX/TAXII, DISARM |
| V. Governance and the Global Landscape | 14-15 | GRC, risk, controls, compliance, global cyber governance, regulation |
| VI. Frontiers and Advanced Practice | 16-20 | AI and agentic runtime security, ATLAS, OT/ICS safety, post-quantum migration, frontier radar, hyper-sophisticated operations, advanced adversary modeling, practitioner tools, version control and secure software delivery, references |

## Interactive Features

- Three top-level panes: Curriculum, Exercises, and Mock Exam.
- A collapsible learning map on desktop and a dismissible navigation drawer on mobile.
- A single compact module rail: reading mode, module jump list, position, and previous/next in one row.
- Generated module tree and reading progress tracking.
- Interactive diagrams with step-through playback, motion-safe signal cues on edges, a per-step readout, and per-diagram open state. Diagram animation pauses automatically when a diagram scrolls out of view.
- Embedded ATT&CK Enterprise, Mobile, and ATLAS matrices with technique detail panels.
- Saved drafts, mastery indicators, and review lists for practice.
- Light theme by default, plus dark and system themes, four accent colours, three reading typefaces, and density, text size, content width, motion, and contrast controls.
- Copyable code blocks and answer reveal controls.

## Exercises And Mock Exam

The Exercises pane is for practice. It includes:

- Section and format filters so learners can drill all questions, one domain, or one format.
- Topic search, mastery filters, saved-for-review flags, and paged rendering that keeps the large bank responsive.
- Multiple choice questions with explanations.
- Open questions with model answers.
- Runnable Python exercises with function contracts, starter code, expected behavior, and automated tests.

The Mock Exam pane is separate and samples from the question bank instead of serving one fixed test. It includes quick and standard attempt lengths, domain and format selection, practice or exam modes, a progress navigator, review flags, timer preferences, resume support, per-domain results, and a compact local history.

## Settings And Local Data

Open Settings from the top bar to control appearance, learning behavior, accessibility, assessment behavior, and local data. Relevant options include:

- Theme, accent colour, interface typeface, information density, text size, and content width.
- Global diagram visibility, default diagram state, diagram animation, motion preference, and high contrast.
- Last-pane memory, advance-on-completion, first-visit walkthrough replay, keyboard shortcuts, exam timer, question navigator, abort confirmation, and the Python runner endpoint.
- A local data summary, JSON backup export, and JSON restore.
- A delete panel that clears one category at a time: reading progress, practice and exam results, saved drafts, preferences, or everything. Each button says exactly what it removes, confirms first, and reloads the page.

The course has no account, analytics service, or remote progress store. Browser state stays on the current device. The optional Python checker listens on `127.0.0.1` and evaluates deterministic tests locally.

## Keyboard Shortcuts

| Key | Action |
|---|---|
| `/` | Focus search |
| `1` | Curriculum |
| `2` | Exercises |
| `3` | Mock Exam |
| `m` | Toggle theme |
| `t` | Back to top |
| `j` | Next section or next module |
| `k` | Previous section or previous module |
| `Esc` | Close a dialog or unfocus an input |

## Project Structure

```text
Cybersecurity_Fundamentals/
+-- README.md
+-- LICENSE
+-- index.html
+-- docker/
|   +-- Dockerfile
|   +-- runner.py
+-- src/
    +-- index.html
    +-- assets/
        +-- overview.png
        +-- open-course.gif
        +-- social-preview.png
```

## Responsible Use

This course is intended for education, defensive learning, authorized security testing, and responsible research only. Offensive concepts are included so defenders can understand, detect, and counter real adversary behavior. Practice only in environments you own, operate, or have explicit written permission to assess.

## License

Released under the MIT License. You may use, modify, teach from, and redistribute this course, including commercially, as long as the copyright and license notice are preserved.
