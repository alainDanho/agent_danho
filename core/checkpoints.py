"""Sauvegardes de fichiers avant modification, avec restauration."""
import shutil
import time
from pathlib import Path

from config import CHECKPOINT_DIR


class CheckpointManager:
    def __init__(self):
        self.history = []

    def snapshot(self, path: Path):
        if not path.exists():
            return
        backup = CHECKPOINT_DIR / f"{path.name}.{int(time.time() * 1000)}.bak"
        shutil.copy2(path, backup)
        self.history.append((str(path), str(backup), time.time()))

    def undo_last(self) -> str:
        if not self.history:
            return "Aucun checkpoint à restaurer."
        original, backup, _ = self.history.pop()
        shutil.copy2(backup, original)
        return f"Restauré : {original}"

    def list_all(self) -> list:
        return list(self.history)
