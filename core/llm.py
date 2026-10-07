"""Appels au modèle via l'API Ollama."""
import requests

from config import OLLAMA_URL


def call_model(messages, model, tools=None, temperature=0.2, timeout=600):
    """Appelle le modèle. Retourne le message assistant complet (dict)."""
    payload = {
        "model": model,
        "messages": messages,
        "stream": False,
        "options": {"temperature": temperature},
    }
    if tools:
        payload["tools"] = tools

    r = requests.post(OLLAMA_URL, json=payload, timeout=timeout)
    r.raise_for_status()
    return r.json()["message"]
