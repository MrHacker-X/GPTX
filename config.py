"""
GPTX configuration.

Every setting can also be supplied as an environment variable -
the environment (or shell export) always takes precedence over
whatever is written in this file.
"""

import os

# ---------------------------------------------------------------
# Required credentials
# ---------------------------------------------------------------

# Your OpenAI API key - https://platform.openai.com/api-keys
# or: export OPENAI_API_KEY="sk-..."
key = os.environ.get("OPENAI_API_KEY", "")

# ---------------------------------------------------------------
# Optional behavior
# ---------------------------------------------------------------

# Chat model used for every question
# or: export GPTX_MODEL="gpt-4o-mini"
MODEL = os.environ.get("GPTX_MODEL", "gpt-4o-mini")

# Maximum tokens in a single reply
# or: export GPTX_MAX_TOKENS="1024"
MAX_TOKENS = int(os.environ.get("GPTX_MAX_TOKENS", "1024"))

# ---------------------------------------------------------------
# Validation - fail fast with a clear message, not a stack trace
# ---------------------------------------------------------------

if not key:
    raise SystemExit(
        "OpenAI API key not configured.\n"
        "  Set key in config.py, or export OPENAI_API_KEY in your shell."
    )
