"""
AutoBackupPy v2 🚀
Développé avec ❤️ par ChatGPT 4 & BonoBeau

📌 Sauvegarde automatique intelligente, portable et configurable pour vos scripts Python.
- Compatible avec la V1 (appel sans paramètre)
- Gestion d'un projet via nameProject
- Nettoyage automatique des anciennes versions
"""

import os
import shutil
from datetime import datetime
import inspect

# Configuration interne (initialisée au premier appel)
_config = {
    "initialized": False,
    "nameProject": "",
    "log": True,
    "limit": 20,
    "horodatage": datetime.now().strftime("%Y%m%d-%H%M%S"),
}


def sauvegardeAuto(nameProject="", LOG_ACTIVE=True, NB_SAUVEGARDE=20):
    """
    Déclenche la sauvegarde automatique du fichier appelant.

    Paramètres :
    - nameProject (str) : Nom du projet pour organiser les sauvegardes ("" par défaut, ou "auto" pour détecter le nom du script principal).
    - LOG_ACTIVE (bool) : Affiche ou non les logs de sauvegarde.
    - NB_SAUVEGARDE (int) : Nombre maximum de sauvegardes à conserver.

    Utilisation simple :
        from sysSauvegarde import sauvegardeAuto
        sauvegardeAuto()

    Utilisation avancée :
        sauvegardeAuto(nameProject="MonProjet", LOG_ACTIVE=False, NB_SAUVEGARDE=10)
    """
    if not _config["initialized"]:
        _config["nameProject"] = nameProject
        _config["log"] = LOG_ACTIVE
        _config["limit"] = NB_SAUVEGARDE
        _config["initialized"] = True

        if _config["nameProject"] == "auto":
            _config["nameProject"] = os.path.basename(
                inspect.stack()[-1].filename
            ).split(".")[0]

    try:
        frame = inspect.stack()[1]
        caller_file = frame.filename
        if not caller_file.endswith(".py"):
            return

        nom_fichier = os.path.basename(caller_file)
        nom_repertoire = os.path.dirname(caller_file)
        dossier_historique = os.path.join(
            nom_repertoire, "Historic", _config["nameProject"], _config["horodatage"]
        )

        if not os.path.exists(dossier_historique):
            os.makedirs(dossier_historique)

        sauvegarde = os.path.join(dossier_historique, nom_fichier)
        shutil.copy2(caller_file, sauvegarde)

        if _config["log"]:
            print(f"✅ Sauvegarde : {sauvegarde}")

        # Nettoyage des anciennes sauvegardes
        if _config["limit"]:
            dossier_parent = os.path.join(
                nom_repertoire, "Historic", _config["nameProject"]
            )
            if os.path.exists(dossier_parent):
                dossiers = sorted(
                    [
                        d
                        for d in os.listdir(dossier_parent)
                        if os.path.isdir(os.path.join(dossier_parent, d))
                    ],
                    reverse=True,
                )
                for ancien in dossiers[_config["limit"] :]:
                    shutil.rmtree(os.path.join(dossier_parent, ancien))

    except Exception as e:
        if _config["log"]:
            print(f"❌ Erreur sauvegardeAuto: {e}")
