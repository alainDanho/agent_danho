# MEMO — Projet agent_danho

Dernière mise à jour : 7 octobre 2026

## 🎯 Objectif du projet

Créer un agent IA local, inspiré de **LM Studio Bionic**, capable de :
- Dialoguer avec un LLM local (via Ollama)
- Lire, écrire et modifier des fichiers
- Exécuter des commandes shell (avec confirmation)
- Rechercher sur le web
- Explorer et installer des modèles Ollama
- Planifier des tâches complexes (plan mode)

**Cible finale** : Mac Intel (Xeon W 16 cœurs, 192 Go RAM, AMD Radeon Pro W5700X 16 Go)
**Machine de dev actuelle** : Mac M1, Python 3.14.7

## 🖥️ Contexte machines

| Machine | Utilisateur | Hostname | Python | Rôle |
|---|---|---|---|---|
| Mac Intel | rti | Mac-Pro-de-DSI-2 | 3.9.6 | Cible de déploiement |
| Mac M1 | admin | 192 | 3.14.7 | Développement actuel |

**Note** : LM Studio et LM Studio Bionic ne supportent PAS les Mac Intel.

**Note** : Pour le déploiement final sur Intel, installer Python 3.12 via python.org et recréer un venv.

## 📦 Stack technique

- **Langage** : Python 3.14 (dev) / 3.12 (cible Intel)
- **Moteur LLM** : Ollama
- **Modèle principal** : qwen2.5:7b (tool calls natifs)
- **Modèle résumé** : qwen2.5:3b
- **Modèle vision** (à venir) : qwen2.5vl:7b
- **Recherche web** : Brave API + fallback DuckDuckGo
- **Dépendances** : requests, python-dotenv

## 📂 Structure du repo
# MEMO — Projet agent_danho

Dernière mise à jour : 7 octobre 2026

---

## 🎯 Objectif du projet

Créer un **agent IA local**, inspiré de LM Studio Bionic, capable de :

- Dialoguer avec un LLM local via Ollama
- Lire, écrire et modifier des fichiers
- Exécuter des commandes shell (avec confirmation)
- Rechercher sur le web (Brave + DuckDuckGo)
- Explorer et installer des modèles Ollama
- Planifier des tâches complexes (plan mode)
- Analyser des images (vision — à venir)
- Interroger des documents locaux (RAG — à venir)
- Déléguer à des sous-agents (à venir)
- Tourner dans un sandbox Docker (à venir)
- Se connecter à des serveurs MCP (à venir)

**Cible finale** : Mac Intel (Xeon W 16 cœurs, 192 Go RAM, AMD Radeon Pro W5700X 16 Go)

**Machine de dev actuelle** : Mac M1 (hostname `192`), Python 3.14.7

---

## 🖥️ Contexte machines

| Machine | Utilisateur | Hostname | Python | Rôle |
|---|---|---|---|---|
| Mac Intel | rti | Mac-Pro-de-DSI-2 | 3.9.6 | Cible de déploiement |
| Mac M1 | admin | 192 | 3.14.7 | Développement actuel |

### Notes critiques

- **LM Studio et LM Studio Bionic ne supportent PAS les Mac Intel.** C'est la raison principale de ce projet : créer un agent maison qui fonctionne sur les deux architectures.
- **Pour le déploiement final sur Intel** : installer Python 3.12 via python.org (installeur universel Intel), puis recréer un venv.
- Le venv n'est pas versionné (dans `.gitignore`), donc chaque machine recrée le sien.
- **Le code doit rester compatible avec Python 3.12** pour pouvoir tourner sur Intel.

---

## 📦 Stack technique choisie

- **Langage** : Python 3.14 (dev) / 3.12 (cible Intel)
- **Moteur LLM** : Ollama (compatible Intel et Apple Silicon)
- **Modèle principal** : `qwen2.5:7b` — supporte les tool calls natifs
- **Modèle résumé** : `qwen2.5:3b` — léger, pour compresser le contexte
- **Modèle vision** (à venir) : `qwen2.5vl:7b`
- **Recherche web** : Brave API (clé gratuite) + fallback DuckDuckGo
- **Dépendances actuelles** : `requests`, `python-dotenv`

### Décisions techniques et pourquoi

| Décision | Raison |
|---|---|
| **Ollama** plutôt que LM Studio | Seul moteur LLM qui tourne sur Mac Intel |
| **qwen2.5:7b** | Bon compromis taille/qualité, supporte les tool calls |
| **Modules séparés** plutôt qu'un gros fichier | Testable, maintenable, lisible |
| **Tool calls natifs** plutôt que parsing regex | Plus fiable, moins de tokens |
| **venv par machine** | Évite les conflits, propre par projet |
| **Brave + DDG fallback** | Brave plus fiable, DDG sans clé en secours |
| **Workspace isolé** | Empêche l'agent de sortir de son dossier |

---

## 📂 Structure du repo

