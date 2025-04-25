# 🚀 AutoBackupPy v2
*Développé avec ❤️ par ChatGPT 4 & BonoBeau*

## 📌 Description
AutoBackupPy est un système de sauvegarde automatique intelligent et léger pour vos scripts Python.  
Chaque script appelant `sauvegardeAuto()` sera sauvegardé dans une structure organisée, idéale pour sécuriser votre travail sans outils de versioning complexes.

AutoBackupPy is a lightweight and smart automatic backup system for your Python scripts.  
It saves every script that calls `sauvegardeAuto()` into a structured folder system, keeping your work safe without complex versioning tools.

---

## ✅ Fonctionnalités / Features
- Paramètres configurables : `nameProject`, `LOG_ACTIVE`, `NB_SAUVEGARDE`
- Initialisation intelligente au **premier appel**
- Option `"auto"` : nom dynamique basé sur le script principal
- Nettoyage automatique (conserve les X dernières sauvegardes)
- Compatibilité V1 (aucun paramètre requis)
- Léger et portable (aucune dépendance)

---

## ⚡ Utilisation / Usage

### Simple (compatible V1)
```python
from sysSauvegarde import sauvegardeAuto
sauvegardeAuto()
```

### Avancé
```python
sauvegardeAuto(nameProject="MonProjet", LOG_ACTIVE=False, NB_SAUVEGARDE=10)
```

### Avec l'option "auto"
```python
sauvegardeAuto(nameProject="auto")
```
Crée une sauvegarde sous :
```
Historic/main/20250425-110000/script.py
```

---

## 🔗 Chaînage : Activer la sauvegarde pour chaque fichier
Pour que **chaque fichier** soit sauvegardé, ajoute ces lignes en haut de **tous les scripts et modules** concernés :

```python
from sysSauvegarde import sauvegardeAuto
sauvegardeAuto()
```

✅ Ainsi, que le fichier soit **exécuté** ou simplement **importé**, il se sauvegardera automatiquement.

> ⚠️ Seul le **premier appel** définit la configuration pour toute la session.

---

## 🗂 Exemple de structure générée
```
Historic/
└── MonProjet/
    └── 20250425-110000/
        ├── main.py
        ├── module.py
        └── utils.py
```

---

## ⚙️ Paramètres
| Paramètre       | Description                                           | Valeur par défaut |
|-----------------|-------------------------------------------------------|-------------------|
| `nameProject`   | Nom du dossier projet (`"auto"` = nom du script)      | `""`              |
| `LOG_ACTIVE`    | Affiche les logs de sauvegarde                        | `True`            |
| `NB_SAUVEGARDE` | Nombre max de dossiers de sauvegarde                  | `20`              |

---

## 💡 Fonctionnement
- **Premier appel** ➜ fixe la configuration globale.
- Chaque fichier appelant `sauvegardeAuto()` se copie dans le dossier de session.
- Le système supprime automatiquement les anciens dossiers au-delà de la limite définie.

---

## 📂 Projet Exemple
Un dossier `/examples` est fourni pour illustrer l'utilisation d'AutoBackupPy dans un mini-projet.

---

## 🔗 Crédits
Développé avec ❤️ par **ChatGPT 4 & BonoBeau**  
> Collaboration, idées intelligentes et rigueur exemplaire 😄
