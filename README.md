# sysbackup / sysSauvegarde.py

🇫🇷 Une bibliothèque Python minimaliste qui permet de sauvegarder automatiquement vos scripts `.py` à chaque exécution, dans un dossier `Historic`.  
🇬🇧 A minimalist Python utility to automatically back up your `.py` scripts at runtime, into a `Historic` subdirectory.

---

## 🔧 Installation

Aucune installation requise, copiez simplement `sysSauvegarde.py` dans votre projet.

---

## 🚀 Utilisation

Ajoutez ces deux lignes au début de n’importe quel script que vous souhaitez sauvegarder :

```python
from sysSauvegarde import sauvegardeAuto
sauvegardeAuto()
```
