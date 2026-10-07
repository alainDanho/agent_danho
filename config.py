"""Configuration centrale du projet."""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/chat")
MODEL = os.environ.get("AGENT_MODEL", "qwen2.5:7b")
SUMMARY_MODEL = os.environ.get("AGENT_SUMMARY_MODEL", "qwen2.5:3b")
VISION_MODEL = os.environ.get("AGENT_VISION_MODEL", "qwen2.5vl:7b")

WORKSPACE = Path(os.environ.get("AGENT_WORKSPACE", "./workspace")).resolve()
WORKSPACE.mkdir(parents=True, exist_ok=True)

CHECKPOINT_DIR = WORKSPACE / ".checkpoints"
CHECKPOINT_DIR.mkdir(exist_ok=True)

MAX_STEPS = 20
CONFIRM_SHELL = True
SUMMARY_THRESHOLD = 40
BRAVE_API_KEY = os.environ.get("BRAVE_API_KEY", "").strip()