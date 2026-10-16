#!/bin/bash
# GPTX setup - detects Termux automatically, works on any Linux/macOS box
# Original by MrHacker-X - modernized setup with dependency verification.

RED='\033[1;31m'
ERR='\033[1;91m'
GREEN='\033[1;92m'
YELLOW='\033[1;33m'
WHITE='\033[1;37m'
RESET='\033[0m'

clear

if [ -f "core/banr" ]; then
    cat core/banr
fi

echo
echo -e "${RED}[+] ${GREEN}Detecting your environment...${RESET}"

if [ -d "/data/data/com.termux/files" ]; then
    echo -e "${RED}[~] ${GREEN}Termux detected - installing dependencies...${RESET}"
    echo
    apt update -y
    apt install python -y
    apt install python-pip -y
    PKG="pkg"
    PIP_FLAGS="--break-system-packages"
elif command -v apt >/dev/null 2>&1; then
    echo -e "${RED}[+] ${GREEN}Debian/Ubuntu-family Linux detected.${RESET}"
    PKG="apt"
    PIP_FLAGS=""
elif command -v dnf >/dev/null 2>&1; then
    echo -e "${RED}[+] ${GREEN}Fedora/RHEL detected.${RESET}"
    PKG="dnf"
    PIP_FLAGS=""
elif command -v pacman >/dev/null 2>&1; then
    echo -e "${RED}[+] ${GREEN}Arch/Manjaro detected.${RESET}"
    PKG="pacman"
    PIP_FLAGS=""
elif command -v apk >/dev/null 2>&1; then
    echo -e "${RED}[+] ${GREEN}Alpine detected.${RESET}"
    PKG="apk"
    PIP_FLAGS=""
else
    echo
    echo -e "${RED}[~] ${YELLOW}No native installer found.${RESET}"
    echo -e "${RED}[~] ${WHITE}Continuing with pip only - assuming Python + pip are already installed.${RESET}"
    PKG=""
    PIP_FLAGS=""
fi

if [ -n "$PKG" ] && ! command -v python3 >/dev/null 2>&1 && ! command -v python >/dev/null 2>&1; then
    echo
    echo -e "${RED}[+] ${GREEN}Installing Python via $PKG...${RESET}"
    case "$PKG" in
        apt)      apt install python3 python3-pip -y ;;
        pkg)      pkg install python -y ;;
        dnf)      dnf install -y python3 python3-pip ;;
        pacman)   pacman -Sy --noconfirm python python-pip ;;
        apk)      apk add --no-cache python3 py3-pip ;;
    esac
fi

PIP=$(command -v pip3 || command -v pip)
if [ -z "$PIP" ]; then
    echo
    echo -e "${RED}[~] ${ERR}ERROR: pip not found.${RESET}"
    echo -e "${RED}[~] ${WHITE}Install pip manually, then run: pip install -r requirements.txt${RESET}"
    exit 1
fi

echo
echo -e "${RED}[+] ${GREEN}Installing Python dependencies...${RESET}"
if [ -n "$PIP_FLAGS" ]; then
    $PIP install $PIP_FLAGS -r requirements.txt || $PIP install --user $PIP_FLAGS -r requirements.txt
else
    $PIP install -r requirements.txt 2>/dev/null || $PIP install --user -r requirements.txt
fi

echo
echo -e "${RED}[+] ${GREEN}Verifying installation...${RESET}"
MISSING=0
for mod in openai rich; do
    if python3 -c "import $mod" 2>/dev/null || python -c "import $mod" 2>/dev/null; then
        echo -e "${RED}[+] ${GREEN}OK: $mod${RESET}"
    else
        echo -e "${RED}[~] ${ERR}MISSING: $mod${RESET}"
        MISSING=$((MISSING + 1))
    fi
done

echo
if [ "$MISSING" -gt 0 ]; then
    echo -e "${RED}[~] ${ERR}$MISSING dependency(ies) failed to install - fix the error(s) above and re-run setup.sh${RESET}"
    exit 1
fi

echo -e "${RED}[+] ${GREEN}GPTX is installed successfully!${RESET}"
echo
echo -e "${RED}[+] ${WHITE}Next steps:${RESET}"
echo -e "${RED}    1. ${GREEN}Edit config.py and put your OpenAI API key in key = \"sk-...\" ${WHITE}(or export OPENAI_API_KEY)${RESET}"
echo -e "${RED}    2. ${GREEN}Run: ${ERR}python3 gptx.py${RESET}"
echo
