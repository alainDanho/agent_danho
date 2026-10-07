"""Registre générique des outils."""


class ToolRegistry:
    def __init__(self):
        self.functions = {}
        self.schemas = []

    def register(self, name, description, parameters, func):
        self.functions[name] = func
        self.schemas.append({
            "type": "function",
            "function": {
                "name": name,
                "description": description,
                "parameters": parameters,
            },
        })

    def call(self, name, args):
        if name not in self.functions:
            return f"Erreur : outil inconnu '{name}'"
        try:
            return str(self.functions[name](**args))
        except Exception as e:
            return f"Erreur d'exécution de {name} : {e}"

    def has(self, name) -> bool:
        return name in self.functions
