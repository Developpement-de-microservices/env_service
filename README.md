# API Gestion des Environnements

Cette API permet de gérer des environnement utiles au déploiement d'applications.

## Endpoints

```POST /environments``` : Création d’un environnement  
```GET /environments``` : Obtenir la liste des environnements   
```GET /environments/{environmentId}``` : Récupérer les informations d’un environnement  
```PATCH /environments/{environmentId}``` : Modification d’un environnement  
```DELETE /environments/{environmentId}``` : Supprimer un environnement   

## Format de donnée

Voici le format de donnée correspondant à l'API Gestion d'Environnements.

```json
{
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "staging-eu-west",
      "type": "development",
      "description": "Good description about environments !",
      "url": "https://example.com/",
      "active": true,
      "createdAt": "2026-03-25T12:36:59.455Z",
      "updatedAt": "2026-03-25T12:36:59.455Z"
    }
}
```