# 🌐 Web Crawler (Python)

Un petit crawler web écrit en Python. Il explore une URL de départ, visite plusieurs pages, extrait tous les liens HTML (`<a href="...">`) valides, et les enregistre automatiquement dans un fichier texte daté.

---

## 🚀 Fonctionnalités

✅ Exploration récursive à partir d'une URL  
✅ Extraction de tous les liens HTTP/HTTPS  
✅ Limite du nombre de pages à visiter  
✅ Sauvegarde des liens dans un fichier `.txt` avec date/heure  
✅ Pause automatique entre chaque requête pour éviter la surcharge du serveur  

---

## 📁 Arborescence du projet

```
web-crawler/
├── crawler.py           # Script principal
├── run_crawler.bat      # Lancement rapide (Windows)
├── requirements.txt     # Dépendances Python
├── .gitignore           # Fichiers à ignorer dans Git
└── README.md            # Ce fichier
```

---

## 📦 Installation

1. **Clone le dépôt** :

```bash
git clone https://github.com/PariaHRZ/web-crawler.git
cd web-crawler
```

2. **Installe les dépendances** :

```bash
pip install -r requirements.txt
```

---

## 🛠️ Utilisation

### 🐍 En ligne de commande

```bash
python crawler.py
```

### 🖱️ Sur Windows

Double-clique sur le fichier `run_crawler.bat`.

---

## ⚙️ Personnalisation

Dans `crawler.py`, tu peux modifier ces deux lignes :

```python
seed_url = "https://example.com"  # URL de départ
links = crawl(seed_url, max_pages=20)  # Nombre de pages à visiter
```

---

## 📁 Résultat

Le script crée automatiquement un dossier `output/` et y enregistre un fichier texte nommé par date et heure, exemple :

```
output/crawled_links_12-05-2025_15-42-07.txt
```

Chaque ligne du fichier correspond à un lien trouvé pendant le crawling.

---

## ⚠️ Avertissement

> ⚠️ Utilise ce crawler uniquement sur des sites que tu es autorisé à explorer.  
> Respecte les conditions d'utilisation et les fichiers `robots.txt` des sites web.

---

## 📜 Licence

Ce projet est sous **[licence MIT](https://github.com/PariaHRZ/web-crawler/blob/main/LICENSE)**.  
Tu peux l'utiliser, le modifier et le partager librement.

---

## 👤 Auteur

Développé par **[PariaHRZ](https://github.com/PariaHRZ)**  
