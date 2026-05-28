FROM python:3.12-slim

RUN useradd --create-home --shell /usr/sbin/nologin runner
WORKDIR /app
COPY runner.py /app/runner.py
USER runner

EXPOSE 8787
CMD ["python", "/app/runner.py"]
