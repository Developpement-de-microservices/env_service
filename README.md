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
      "id": "69ce634e9e3ccbbb39759219",
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
| id           | Identifiant unique MongoDB         |
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
* Utiliseation d'un conteneur MongoDB pour le stockage des environnements
* Communication via REST
* Intégré avec :

  * /users

---

## Remarques

* Le champ `active` ne peut être que true ou false, soit actif ou nonSS
* Les identifiants sont générés epar MongoDB (conversion des clé primaires en ID)
* Ce service est conçu pour être utilisé avec un proxy dans l’architecture globale

---