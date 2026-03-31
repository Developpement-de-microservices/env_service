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