# Projet Django - Gestion scolaire (School IDAI)

Projet de gestion scolaire réalisé avec Django dans un niveau simple, propre et réaliste d'étudiant en **Licence IDAI - FST Tanger**.

## 1. Contenu du projet

Le projet contient 3 applications principales :

- `home_auth` : authentification, rôles et tableau de bord
- `student` : gestion des parents et des étudiants
- `faculty` : gestion des enseignants, départements, matières, congés, emplois du temps, examens et résultats

## 2. Prérequis

Avant de lancer le projet, il faut avoir :

- Python installé
- pip installé
- un terminal (PowerShell, CMD ou terminal VS Code)

## 3. Installation du projet

### Windows

```bash
python -m venv monenv
monenv\Scripts\activate
pip install -r requirements.txt
```

### Linux / Mac

```bash
python3 -m venv monenv
source monenv/bin/activate
pip install -r requirements.txt
```

## 4. Préparation de la base de données

Exécuter les commandes suivantes :

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Génération des données de test

Le projet contient une commande personnalisée qui crée automatiquement des données de démonstration.

```bash
python manage.py seed_school
```

Cette commande crée :

- 1 compte administrateur
- 1 compte enseignant
- 1 compte étudiant
- quelques départements
- quelques matières
- un parent
- un étudiant
- un enseignant
- un congé
- un emploi du temps
- un examen
- un résultat d'examen

## 6. Lancement du projet

Après les migrations et les données de test :

```bash
python manage.py runserver
```

Puis ouvrir dans le navigateur :

- Accueil : `http://127.0.0.1:8000/`
- Connexion : `http://127.0.0.1:8000/login/`
- Administration Django : `http://127.0.0.1:8000/admin/`

## 7. Identifiants de test

### Administrateur
- **Nom d'utilisateur :** `admin`
- **Mot de passe :** `admin12345`

### Enseignant
- **Nom d'utilisateur :** `teacher1`
- **Mot de passe :** `teacher12345`

### Étudiant
- **Nom d'utilisateur :** `student1`
- **Mot de passe :** `student12345`

## 8. Structure du projet

```text
school_management_idai/
├── manage.py
├── requirements.txt
├── README.md
├── .gitignore
├── home_auth/
├── student/
├── faculty/
├── school/
├── templates/
├── static/
└── faculty/management/commands/seed_school.py
```

## 9. Données de test

Pour les données de test, le projet utilise la commande suivante :

```bash
python manage.py seed_school
```

Cette commande joue le rôle de script de préparation des données de démonstration.

## 10. Dépôt GitHub public

(https://github.com/Charaf9999/projet-school-management-idai)

Le dépôt doit contenir au minimum :

- le projet Django complet
- `requirements.txt`
- `README.md`
- les données de test via la commande `seed_school`

## 11. Lien de la vidéo de démonstration


**Lien de la vidéo :** `À compléter avant la remise`


"# projet-school-management-idai" 
