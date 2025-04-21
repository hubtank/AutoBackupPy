"""
Bibliothèque : sysSauvegarde

📌 Objectif :
Cette bibliothèque permet la sauvegarde automatique de tout fichier Python qui l'importe et appelle `sauvegardeAuto()`.
Elle crée une copie du script en cours d'exécution dans un sous-dossier `Historic/`, en conservant uniquement les 20 dernières versions.
Très utile pour éviter la perte de travail ou retrouver une version antérieure d'un fichier sans versionning complexe.

✅ Utilisation :
Ajouter simplement au début d’un script (ou module) :
    from sysSauvegarde import sauvegardeAuto
    sauvegardeAuto()

Cela déclenchera automatiquement une sauvegarde de ce fichier.

🌍 Compatibilité :
Cette bibliothèque est compatible avec tous les environnements Python standard (y compris Pythonista, VSCode, terminal, etc.) à condition que les permissions d'écriture soient valides dans le dossier d'exécution.

🗃 Limitation :
Ne gère que les fichiers `.py` exécutés directement ou importés.

"""

import os
import shutil
from datetime import datetime
import inspect


def sauvegardeAuto():
    try:
        # Détecte automatiquement le fichier appelant
        frame = inspect.stack()[1]
        caller_file = frame.filename
        if not caller_file.endswith(".py"):
            return  # Ignore si ce n’est pas un fichier Python

        nom_fichier = os.path.basename(caller_file)
        nom_repertoire = os.path.dirname(caller_file)
        dossier_historique = os.path.join(nom_repertoire, "Historic")

        # Crée le dossier Historic s’il n’existe pas
        if not os.path.exists(dossier_historique):
            os.mkdir(dossier_historique)

        # Format du nom de sauvegarde
        horodatage = datetime.now().strftime("%Y%m%d-%H%M%S")
        sauvegarde = os.path.join(
            dossier_historique, f"{nom_fichier[:-3]}_{horodatage}.py"
        )

        # Copie le fichier
        shutil.copy2(caller_file, sauvegarde)

        # Ne garde que les 20 dernières sauvegardes pour ce fichier
        sauvegardes = sorted(
            [
                f
                for f in os.listdir(dossier_historique)
                if f.startswith(nom_fichier[:-3])
            ],
            reverse=True,
        )
        for ancienne in sauvegardes[20:]:
            os.remove(os.path.join(dossier_historique, ancienne))
    except Exception as e:
        print(f"❌ Erreur dans sauvegardeAuto: {e}")
