# Environnement Service – SAE401

Microservice de gestion des environnements liés aux déploiements dans la plateforme de gestion des déploiements d’applications.

---

## Description

Le service **Environnement** permet de créer, de modifier et de consulter tous les environnements.

Il sert principalement à :

* Afficher la liste d'environnements, un environnements précis
* Créer et modifier un environnement

---

## Fonctionnalités

* Création d’un environnement
* Consultation d’un environnement
* Liste des environnement
* Modification d'un environnement
* Filtrage par :
  * id
* Vérification de la santé de l'application
---

## Modèle de données

### Envrironnement

```json
    {
      "id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
      "name": "prod-eu-west",
      "type": "production",
      "description": "Environnement de production d'europe de l'ouest",
      "url": "https://example.com/",
      "active": true,
      "createdAt": "2026-03-25T12:30:04.763Z",
      "updatedAt": "2026-03-25T12:30:04.763Z"
    }
```

### Champs

| Champ        | Description                        |
| ------------ | ---------------------------------- |
| id           | Identifiant unique (UUID)          |
| name         | Nom de l'environnement             |
| type         | Type d’environnement               |
| description  | Description lisible                |
| url          | URL de l'environnement             |
| active       | Status de l'environnement          |
| createdAt    | Date de création                   |
| updatedAt    | Date de modification               |

---

## Architecture

* Microservice indépendant
* Communication via REST / JSON
* Intégré avec :

  * /users

---

## Remarques

* Le champ `active` ne peut être que true ou false, soit actif ou nonSS
* Les identifiants sont générés en UUID
* Ce service est conçu pour être utilisé avec un proxy dans l’architecture globale

---