# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

## [1.0] - 31/03/2026
### Added
- Création du service **Environnement** en Flask.
- Gestion des environnement :
  - Liste de tous les environnements (`/environnements` - GET)
  - Liste d'un environnement par ID (`/environnements/<id>` - GET)
  - Création d’un environnement (`/environnements` - POST)
  - Modification d’un environnement par son ID (`/environnements/<id>` - PATCH)
- Validation des champs obligatoires : `name`, `type`.
- Vérification de l’existence des IDs en interne et via le service **Users**.
- Stockage persistant des environnements dans `envs.json`.
- Authentification et vérification des tokens via le service `/auth/verify`.
- Endpoint **health** pour le service Events (`/environnements/health`).
- Gestion des erreurs : service injoignable, ID inexistant, champ manquant, type invalide.

### Changed
- N/A (première version)

### Fixed
- N/A (première version)

## [2.0] - 02/04/2026
### Added
- Création d'un conteneur MongoDB :
  - Stocke les environnements dans une base de donnée
  - ID uniques
- Gestion des erreurs : pas de donnée entrée lors de la modification, aucun environnement existant.
- Création d'une fonction de vérification du token de connexion.

### Changed
- Modification du système de stockage de donnée :
  - Utilisation de MongoDB à la place de JSON local.
- Conteneur spécifique à cette nouvelle base de donnée.
- Réseau spécifique entre le microservice et la base de donnée.
- Suppression du volume partagé.
- Méthode de vérification du token de connexion sur chaque route.
- Changement de l'image Docker utilisée dans le Dockerfile par une image plus légère
```Dockerfile
python:3.14-alpine3.23
```

### Fixed
- Fix de la fonction de vérification de token pour s'adapter au token dynamique.
- Fix de la gestion d'erreur lorsqu'il n'y a pas de donnée pour la modification.
- Vérification des IDs sur chaque fonction qui cherche par ID.