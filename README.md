# Course on Cybersecurity Fundamentals

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square" alt="MIT Licensed" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Type-HTML_Course-4f46e5.svg?style=flat-square" alt="Single HTML Course" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Build-No_Build_Step-16a34a.svg?style=flat-square" alt="No Build Step" /></a>
  <a href="#"><img src="https://img.shields.io/badge/Includes-Labs_Exercises_Mock_Exam-f97316.svg?style=flat-square" alt="Labs, Exercises, and Mock Exam" /></a>
</p>

A free, browser-based course on cybersecurity fundamentals. It covers practical security foundations across cryptography, networks, web security, ATT&CK, detection engineering, DFIR, malware, threat intelligence, DISARM, cloud, identity, governance, hands-on exercises, and a sampled mock exam.

![Course overview](src/assets/overview.png)

## Repository Description

Use this GitHub repository description:

> MIT-licensed cybersecurity fundamentals course in one interactive HTML file, covering crypto, networks, web security, ATT&CK, DFIR, malware, CTI, DISARM, GRC, labs, exercises, and a sampled mock exam.

## Contents

- [Quick Start](#quick-start)
- [What Is Included](#what-is-included)
- [Course Structure](#course-structure)
- [Interactive Features](#interactive-features)
- [Exercises And Mock Exam](#exercises-and-mock-exam)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Project Structure](#project-structure)
- [Responsible Use](#responsible-use)
- [License](#license)
- [Contributing](#contributing)

## Quick Start

There is nothing to install.

```bash
# Clone the repository, then open the course
open src/index.html          # macOS
xdg-open src/index.html      # Linux
start src/index.html         # Windows
```

You can also open the root `index.html`, which redirects to the course in `src/`.

Progress, lab drafts, theme, and exam work are saved locally in your browser with `localStorage`. No account, backend, telemetry, or build step is required.

## What Is Included

- Practical cybersecurity fundamentals with enough depth for serious self-study.
- A searchable curriculum with 19 modules.
- Code labs with hints, saved drafts, and model solutions.
- Realistic exercises based on cases such as APT28-style tradecraft, botnet C2, cloud SSRF, ransomware, and supply-chain compromise.
- MITRE ATT&CK content, technique mapping, detection engineering, Navigator-style coverage logic, and Sigma examples.
- Threat intelligence interoperability: STIX 2.1, TAXII 2.1, MISP, OpenCTI, markings, confidence, expiry, and dissemination controls.
- DISARM-style influence operation analysis for FIMI, hack-and-leak operations, amplification, and evidence handling.
- Governance and risk coverage: NIST CSF 2.0, ISO 27001, CIS Controls, FAIR, CVSS, EPSS, KEV, GDPR, NIS2, DORA, SEC cyber disclosure, PCI DSS, HIPAA, and SOC 2.

## Course Structure

| Part | Modules | Focus |
|---|---:|---|
| I. Foundations and the Adversary | 01-02 | Security properties, risk, threat actors, cybercrime economy |
| II. Technical Core | 03-05 | Cryptography, network security, traffic analysis, web application security |
| III. Offensive Operations | 06-07 | MITRE ATT&CK, reconnaissance, phishing, exploitation, lateral movement, C2 |
| IV. Defensive Operations and Intelligence | 08-11 | SOC, detection engineering, DFIR, malware, ransomware, CTI, STIX/TAXII, DISARM |
| V. Governance, Identity, Cloud, and Frontiers | 12-15 | GRC, IAM, cloud, containers, AI security, OT/ICS, post-quantum migration |
| VI. Advanced Operations and Global Governance | 16-19 | Stuxnet, adversary modeling, practitioner tools, global cyber governance, references |

## Interactive Features

- Three top-level panes: Curriculum, Exercises, and Mock Exam.
- All-modules mode or module-by-module mode with previous and next navigation.
- Generated module tree and reading progress tracking.
- Embedded ATT&CK matrix with technique detail panels.
- Saved lab drafts so work is not lost on refresh.
- Light and dark themes.
- Copyable code blocks and answer reveal controls.

## Exercises And Mock Exam

The Exercises pane contains guided tutor-style practice cases. The Mock Exam pane samples from the question bank instead of serving one fixed test.

The mock exam supports:

- Multiple choice, open response, and coding questions.
- Practice mode with immediate tutor feedback.
- Exam mode with feedback withheld until grading.
- Random or domain-sectioned attempts.
- Weighted scoring normalized to a 1000-point scale, with 700 as the target readiness score.
- Per-domain breakdowns so weak areas become a study plan.

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
+-- src/
    +-- index.html
    +-- assets/
        +-- overview.png
```

## Responsible Use

This course is intended for education, defensive learning, authorized security testing, and responsible research only. Offensive concepts are included so defenders can understand, detect, and counter real adversary behavior. Practice only in environments you own, operate, or have explicit written permission to assess.

## Ongoing Work In Progress

This course is actively maintained. Content, labs, mappings, screenshots, and mock-exam items may change as the material is reviewed, expanded, and improved. Issues and pull requests are welcome, especially improvements to technical accuracy, lab quality, ATT&CK mappings, CTI interoperability, DISARM examples, regulatory explanations, and realistic case exercises. Keep the project dependency-free and vendor-neutral.

## License

Released under the MIT License. You may use, modify, teach from, and redistribute this course, including commercially, as long as the copyright and license notice are preserved.
