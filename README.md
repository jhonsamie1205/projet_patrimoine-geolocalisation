# 🗺️ Projet Patrimoine & Géolocalisation

Application web de cartographie et de gestion des sites patrimoniaux, développée dans le cadre de ma formation en informatique à l'Institut Africain d'Informatique (IAI).

---

## 📌 Description

Cette application permet de **localiser et visualiser des sites patrimoniaux** sur une carte interactive. Les données sont stockées dans une base de données MySQL et affichées dynamiquement via une interface web.

---

## ✨ Fonctionnalités

- Affichage des sites patrimoniaux sur une carte interactive
- Insertion et gestion des données via une base de données MySQL
- Génération dynamique de la carte à partir des données
- Interface web responsive en HTML/CSS

---

## 🛠️ Technologies utilisées

| Couche | Technologie |
|--------|------------|
| Backend | Python |
| Base de données | MySQL |
| Frontend | HTML, CSS |
| Cartographie | Python (génération de carte) |

---

## 📁 Structure du projet

```
projet_patrimoine-geolocalisation/
│
├── templates/          # Pages HTML (frontend)
├── static/             # Fichiers CSS et ressources statiques
├── table sql/          # Scripts SQL (création des tables)
│
├── acces_bd.py         # Connexion et requêtes à la base de données
├── insertion_bd.py     # Insertion des données dans la BD
├── generer_carte.py    # Génération de la carte interactive
└── essay.py            # Tests et essais
```

---

## 🚀 Installation et lancement

### Prérequis

- Python 3.x
- MySQL
- Un navigateur web

### Étapes

1. Clone le dépôt :
   ```bash
   git clone https://github.com/jhonsamie1205/projet_patrimoine-geolocalisation.git
   cd projet_patrimoine-geolocalisation
   ```

2. Installe les dépendances Python :
   ```bash
   pip install mysql-connector-python folium
   ```

3. Crée la base de données en exécutant les scripts SQL du dossier `table sql/`

4. Configure les paramètres de connexion dans `acces_bd.py`

5. Lance l'application :
   ```bash
   python generer_carte.py
   ```

---

## 👨‍💻 Auteur

**Samie Essoniwa Jonathan**
- GitHub : [@jhonsamie1205](https://github.com/jhonsamie1205)
- LinkedIn : [linkedin.com/in/esso-john4691](https://www.linkedin.com/in/esso-john4691)
- Email : jhonsamie1205@gmail.com

---

## 📄 Licence

Projet réalisé dans un cadre académique — Institut Africain d'Informatique, Lomé, Togo.
