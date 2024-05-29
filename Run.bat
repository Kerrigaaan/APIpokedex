@echo off

REM Créer un environnement virtuel dans le dossier du projet
echo Création de l'environnement virtuel...
python -m venv env

REM Activer l'environnement virtuel
echo Activation de l'environnement virtuel...
call env\Scripts\activate

REM Installer les dépendances depuis requirements.txt
echo Installation des dépendances...
pip install -r requirements.txt

REM Exécuter le script import_bd.py
echo Importation des données dans la base de données...
python .\BDD\import_bd.py

REM Lancer l'application FastAPI avec uvicorn
echo Lancement de l'application...
uvicorn app.main:app --reload

REM Désactiver l'environnement virtuel après utilisation
echo Désactivation de l'environnement virtuel...
deactivate

echo Toutes les tâches sont terminées.
pause

