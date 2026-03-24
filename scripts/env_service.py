from flask import Flask, jsonify, request
import json
from datetime import datetime
import zoneinfo

def load_env():                                                   # Fonction qui charge les environnements depuis le fichier d'environnements
    with open("../data/envs.json", "r") as f:
        return json.load(f)
    
def save_env(envs):                                                # Fonction qui sauvegarde les environnements dans le fichier d'environnements
    with open("../data/envs.json", "w") as f:
        json.dump(envs, f ,indent=4)

app = Flask(__name__)

@app.route("/envs", methods=["POST"])
def create_env():
    
    user_data = request.get_json()

    env_name = user_data.get("name")                              #On les stock dans des variables séparée
    env_description = user_data.get("description")

    envs = load_env()

    ids = []

    for env in envs:
        ids.append(env.get("id", 0))

    last_id = max(ids, default=0)

    paris_tz = zoneinfo.ZoneInfo("Europe/Paris")                  # On récupère la timezone demandé
    now = datetime.now(paris_tz)                                  # On récupère la date en fonction de la timezone
    env_created = now.strftime("%Y-%m-%dT%H:%M:%S%z")             # On met la date dans une variable que nous allons mettre dans l


    new_env = {                                                   # On créer un nouvel environnement avec le dernier ID + 1 et les donnée entrée par l'utilisateur
        "id": last_id+1,
        "name": env_name,
        "description": env_description,
        "created_at": env_created
    }

    envs.append(new_env)                                          # On ajoute cet environnement à la fin de liste (qui correspond au fichier)

    save_env(envs)

    return jsonify(new_env), 200

@app.route("/envs", methods=["GET"])
def list_env():

    env = load_env()                                              # On charge le fichier des environnements
    return env, 200

@app.route("/envs/<int:envId>", methods=["GET"])
def detail_env():
    return "GET /envs/envId"

@app.route("/envs/<int:envId>", methods=["PUT"])
def update_env():
    return "PUT /envs/envId"

@app.route("/envs/<int:envId>", methods=["DELETE"])
def del_env():
    return "DELETE /envs/envId"


if __name__ == '__main__':                                          # On définit les paramètres de notre programme, comme l'adresse qu'il utilise et le port utilisé
    app.run(host="0.0.0.0", port=5000)