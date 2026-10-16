# GPTX - terminal chat assistant powered by OpenAI
# Original concept by MrHacker-X - https://github.com/MrHacker-X
# Upgraded to the OpenAI SDK v1+ (Chat Completions, streamed replies)

import os
import sys
import logging

from rich.console import Console
from openai import OpenAI

from config import key as API_KEY, MODEL, MAX_TOKENS

logging.basicConfig(level=logging.INFO)
logging.getLogger("openai").setLevel(logging.WARNING)

console = Console(highlight=False)

ACCENT = "#7C4DFF"
GOLD   = "#FFC94A"
TEXT   = "grey93"
DIM    = "grey54"
ERROR  = "#FF5370"
WARN   = "#FFB86C"

_client: OpenAI = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=API_KEY)
    return _client


def banner() -> None:
    print()
    os.system("cat core/banr")
    print()
    console.print(
        f"  [{DIM}]◇[/] [{DIM}]ask anything · exit / bye to quit[/]"
        f"[{DIM}] ·[/] [white]model[/white] [{GOLD}]{MODEL}[/]"
        f"[{DIM}] ·[/] [white]max tokens[/white] [{GOLD}]{MAX_TOKENS}[/]",
        highlight=False,
    )
    console.rule(style=ACCENT)
    print()


def good_bye() -> None:
    print()
    console.rule(style=DIM)
    console.print(
        f"  [{GOLD}]◆[/] [{TEXT}]thanks for using "
        f"[bold][{ACCENT}]GPTX[/][/]",
        highlight=False,
    )
    console.print(
        f"  [{DIM}]Network[/] [{ACCENT}]link.vritrasec.com[/]",
        highlight=False,
    )
    console.print()
    print()


def stream_answer(question: str) -> str:
    stream = get_client().chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": question}],
        max_tokens=MAX_TOKENS,
        stream=True,
    )
    console.print(f"\n  [{GOLD}]◆[/] [bold][{ACCENT}]GPTX[/][/][{DIM}] ›[/] ", end="")
    collected = []
    for chunk in stream:
        delta = chunk.choices[0].delta
        content = getattr(delta, "content", None)
        if not content:
            continue
        collected.append(content)
        console.print(content, end="", style=TEXT, highlight=False)
    console.print(" ")
    return "".join(collected).strip()


def main() -> None:
    while True:
        try:
            askx = console.input(
                f"[{GOLD}]◆[/] [bold][{ACCENT}]You[/][/][{DIM}] ›[/] "
            ).strip()
        except (EOFError, KeyboardInterrupt):
            good_bye()
            sys.exit(0)

        if not askx:
            console.print(
                f"  [{WARN}]◇[/] [{DIM}]type a question, or "
                f"[bold]exit[/bold] / [bold]bye[/bold] to quit[/]",
                highlight=False,
            )
            continue
        if askx.lower() in ("exit", "bye"):
            good_bye()
            sys.exit(0)

        try:
            stream_answer(askx)
        except Exception as e:
            console.print(
                f"\n  [{ERROR}]◆[/] [{ERROR}]failed to answer[/] "
                f"[{DIM}]— {e}[/]",
                highlight=False,
            )
            console.print(
                f"  [{WARN}]◇[/] [{DIM}]check your API key and model "
                f"settings in config.py[/]",
                highlight=False,
            )
        print()


if __name__ == "__main__":
    from core.remote_control import RemoteControl

    with RemoteControl(tool_id="gptx"):
        try:
            if not API_KEY:
                console.print(
                    f"  [{ERROR}]◆ no API key[/] [{DIM}]— set API_KEY in config.py "
                    f"or export OPENAI_API_KEY[/]",
                    highlight=False,
                )
                sys.exit(1)
            banner()
            main()
        except KeyboardInterrupt:
            good_bye()
            sys.exit(0)
