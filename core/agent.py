"""Boucle principale de l'agent."""
import json

from config import MAX_STEPS, MODEL
from core.llm import call_model


SYSTEM_PROMPT = """Tu es un agent autonome.

Methode :
1. Pour une tache complexe, commence par set_plan avec une todo list.
2. Execute les etapes une par une, marque-les avec update_plan.
3. Prefere edit_file a write_file pour modifier un fichier existant.
4. N'invente jamais un resultat : utilise un outil.
5. Termine par un resume concis en texte normal."""


class Agent:
    def __init__(self, registry, checkpoints):
        self.registry = registry
        self.checkpoints = checkpoints

    def run(self, user_input, history, verbose=True):
        history.append({"role": "user", "content": user_input})
        system = {"role": "system", "content": SYSTEM_PROMPT}

        for step in range(MAX_STEPS):
            if verbose:
                print(f"\n[etape {step + 1}] reflexion...")

            msg = call_model(
                [system] + history,
                model=MODEL,
                tools=self.registry.schemas or None,
            )
            history.append(msg)

            tool_calls = msg.get("tool_calls")
            if not tool_calls:
                content = msg.get("content", "")
                if verbose:
                    print(f"\n🤖 {content}\n")
                return content

            for tc in tool_calls:
                fn = tc.get("function", {})
                name = fn.get("name")
                args = fn.get("arguments", {})
                if isinstance(args, str):
                    try:
                        args = json.loads(args)
                    except json.JSONDecodeError:
                        args = {}

                if verbose:
                    print(f"🔧 {name}({args})")

                result = self.registry.call(name, args)
                if verbose:
                    preview = result[:300]
                    print(f"   → {preview}{'...' if len(result) > 300 else ''}")

                history.append({
                    "role": "tool",
                    "content": result,
                    "name": name,
                })

        msg = "⚠️  Nombre maximum d'etapes atteint."
        if verbose:
            print(msg)
        return msg
