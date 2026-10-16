<div align="center">

# ⃤ G P T X ⃤

### *ChatGPT in your terminal - one prompt loop, streamed answers, zero web UI.*

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/AI-OpenAI%20Chat%20API-412991?style=flat-square&logo=openai&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20macOS-38;5;150?style=flat-square)
![Streaming](https://img.shields.io/badge/Answers-streamed-38;5;245?style=flat-square)
![Stars](https://img.shields.io/github/stars/MrHacker-X/GPTX?style=flat-square&color=orange)
![Forks](https://img.shields.io/github/forks/MrHacker-X/GPTX?style=flat-square&color=cyan)

</div>

---

## 📋 Table of Contents

- [🎯 Why GPTX?](#-why-gptx)
- [🧭 What It Does](#-what-it-does)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [✨ Features](#-features)
- [⌨️ Usage](#%EF%B8%8F-usage)
- [⚙️ Configuration](#%EF%B8%8F-configuration)
- [🧰 Tech Stack](#-tech-stack)
- [⚠️ Disclaimer](#%EF%B8%8F-disclaimer)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [👨‍💻 Developer](#-developer)

---

## 🎯 Why GPTX?

> Everything you need from ChatGPT fits into one terminal loop: type a question, get the answer, repeat. **GPTX is that loop** - no browser tabs, no API playground, no framework.
>
> **v2.0 modernizes the engine.** Built on the **OpenAI SDK v1+ Chat Completions API** (`gpt-4o-mini` default), replies **stream into the terminal as they generate**, wrapped in a premium violet-gold rich theme with per-loop error containment and fail-fast config validation. Setup detects Termux and four Linux package-manager families automatically, and verifies every dependency before claiming success.

---

## 🧭 What It Does

| # | Step | What happens |
|---|------|-------------|
| 1️⃣ | **Ask** | You type a question in the terminal (`◆ You ›`) |
| 2️⃣ | **Stream** | The OpenAI chat model replies, printing token-by-token (`◆ GPTX ›`) |
| 3️⃣ | **Loop** | Ask again, `exit` / `bye` when done - Ctrl+C / Ctrl+D also exit cleanly |

**What this tool is NOT:** it is **not** a group-bot platform, **not** a reseller frontend, and **not** a way around OpenAI's usage policies - you are responsible for what you ask.

---

## 🚀 Quick Start

```bash
git clone https://github.com/MrHacker-X/GPTX.git
cd GPTX
./setup.sh                      # installs deps (Termux / apt / dnf / pacman / apk)
nano config.py                  # or: export OPENAI_API_KEY="sk-..."
python3 gptx.py                 # chat loop starts
```

<details>
<summary><b>🔑 Where do I get an API key?</b></summary>

Create one at [platform.openai.com/api-keys](https://platform.openai.com/api-keys) - every question is billed to that key, so keep it private.

</details>

---

## 📦 Installation

### Termux (Android)

```bash
apt update -y && apt install git -y
git clone https://github.com/MrHacker-X/GPTX.git
cd GPTX
chmod +x setup.sh
./setup.sh
```

### Desktop Linux / macOS

```bash
git clone https://github.com/MrHacker-X/GPTX.git
cd GPTX
./setup.sh          # or: pip install -r requirements.txt
```

### Supported Systems

| OS | Status | Notes |
|----|--------|-------|
| 📱 Termux (Android) | ✅ Fully supported | Auto-detected |
| 🐧 Debian / Ubuntu / Kali | ✅ Fully supported | `apt` detected automatically |
| 🐧 Fedora / RHEL | ✅ Fully supported | `dnf` detected automatically |
| 🐧 Arch / Manjaro | ✅ Fully supported | `pacman` detected automatically |
| 🐧 Alpine | ✅ Fully supported | `apk` detected automatically |
| 🍎 macOS | ✅ Fully supported | pip-only path, needs Python preinstalled |

> 💡 The setup script **verifies every dependency** at the end and tells you exactly what's missing - it will never print "installed successfully" when it isn't.

---

## ✨ Features

| | Feature | Description |
|---|---------|-------------|
| 💬 | **Streamed answers** | Chat Completions stream token-by-token into the terminal - no long silent waits |
| 🧠 | **Modern chat models** | `gpt-4o-mini` default; any OpenAI chat model via config |
| 🎨 | **Premium color theme** | Custom violet-gold rich palette with live generation indicators |
| 🛡️ | **Error containment** | A failed API call reports and returns to the prompt - the loop never crashes out |
| 🩹 | **Fail-fast validation** | Missing API key → one clear line at startup, no stack trace |
| 🧹 | **Clean exits** | `exit`, `bye`, Ctrl+C and Ctrl+D all leave gracefully |
| 🔑 | **Env-var credentials** | Key supplied via `config.py` placeholder or environment variables — a real key never ships in the repo |
| 🪶 | **Minimal dependencies** | 2 packages: `openai`, `rich` |

---

## ⌨️ Usage

Run the tool, ask anything:

```bash
python3 gptx.py
```

| Input | Result |
|-------|--------|
| any question | e.g. `explain DNS in one paragraph` → streamed GPTX answer |
| empty input | Gentle hint, loop continues |
| `exit` or `bye` | Exits with links to the developer's channels |
| Ctrl+C / Ctrl+D | Same clean exit - no traceback |

---

## ⚙️ Configuration

Everything lives in [`config.py`](config.py) - and every setting can be overridden from the shell:

| Setting | Env var | Default | Description |
|---------|---------|---------|-------------|
| API key | `OPENAI_API_KEY` | *(required)* | Your OpenAI API key (`key` inside config.py) |
| Model | `GPTX_MODEL` | `gpt-4o-mini` | Any OpenAI chat model |
| Max tokens | `GPTX_MAX_TOKENS` | `1024` | Length cap per reply |

```bash
# either edit config.py, or:
export OPENAI_API_KEY="sk-..."
export GPTX_MODEL="gpt-4o"
```

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.8+ |
| AI | `openai` SDK v1+ — streamed Chat Completions |
| Terminal UI | `rich` — custom violet/gold theme (truecolor, graceful degradation) |
| Setup | POSIX bash with 5 environment detections |

---

## ⚠️ Disclaimer

> ### Read this before using GPTX.
>
> 1. **You pay per token.** Every question is billed to your OpenAI key. Keep the key private and the token cap sane.
> 2. **OpenAI's policies apply.** Your prompts must comply with OpenAI's [usage policies](https://openai.com/policies) - you are responsible for what you ask.
> 3. **Personal use.** GPTX is a personal assistant tool, not a service for third parties.
> 4. **No warranty.** Provided "as is", with no warranty of any kind. The author is **not liable** for any misuse, cost, or damage resulting from its use.

---

## 🤝 Contributing

Contributions are welcome!

```bash
# 1. fork it
# 2. create your branch
git checkout -b feature/amazing-feature
# 3. commit
git commit -m "Add amazing feature"
# 4. push
git push origin feature/amazing-feature
# 5. open a Pull Request
```

Ideas worth exploring: per-session conversation memory, markdown rendering for code-heavy answers, a `/clear` command, one-shot `--ask "..."` CLI mode for scripts.

---

## 📜 License

Distributed under the MIT License. See the [`LICENSE`](LICENSE) file for the full text.

---

## 👨‍💻 Developer

| | |
|---|---|
| **Dev** | MrHacker-X |
| **GitHub** | [github.com/MrHacker-X](https://github.com/MrHacker-X) |
| **Email** | [contact@vritrasec.com](mailto:contact@vritrasec.com) |
| **Website** | [vritrasec.com](https://vritrasec.com) |
| **Network** | [link.vritrasec.com](https://link.vritrasec.com) |

---

<div align="center">

### ⭐ Star the repo if GPTX answered you well ⭐

*Built by MrHacker-X - chat power, terminal simplicity.*

</div>
