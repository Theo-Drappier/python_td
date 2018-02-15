# INSTALLATION
git clone https://github.com/Theo-Drappier/python_td.git

Dans le dossier qui vient d'être cloné :
pip install -r requirements.txt
(si un traceback apparaît et affiche un "permission denied" il faut faire : pip install -r requirements.txt --user)

Il faut créer la base de données prog_agent_v0 et importer le fichier prog_agent_v0.sql dans celle-ci.
Dans le fichier models/Connection.py, rentrez vos informations de base de données (utilisateurs, mdp et url).

Dernière étape :
FLASK_APP=server.py flask run
Si vous voulez ajouter des données de votre hôte, il faut run index.py

Well done. L'application devrait fonctionné.
