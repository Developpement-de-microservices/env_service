# API Gestion des Environnements

Cette API permet de gérer des environnement utiles au déploiement d'applications.

## Endpoints

```POST /envs``` : Création d’un environnement  
```GET /envs``` : Obtenir la liste des environnements   
```GET /envs/{envId}``` : Récupérer les informations d’un environnement  
```PUT /envs/{envId}``` : Modification d’un environnement  
```DELETE /envs/{envId}``` : Supprimer un environnement   

## Format de donnée

Voici le format de donnée correspondant à l'API Gestion d'Environnements.

```json
{
  "id": 1,
  "name": "production",
  "description": "Environnement live",
  "created_at": "2024-01-10T12:00:00Z"
}
```