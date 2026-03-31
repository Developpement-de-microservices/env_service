from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
import uuid
import json
from datetime import datetime, timezone

def load_env():                                                   # Fonction qui charge les environnements depuis le fichier d'environnements
    with open("./data/envs.json", "r") as f:
        return json.load(f)
    
def save_env(envs):                                                # Fonction qui sauvegarde les environnements dans le fichier d'environnements
    with open("./data/envs.json", "w") as f:
        json.dump(envs, f ,indent=4)

app = Flask(__name__)
CORS(app)

@app.route("/environments/health", methods=["GET"])
def heath_env():
    return jsonify({"status": "ok","service": "Environnements","timestamp": "2026-03-31T08:11:20.395Z"}), 200

@app.route("/environments", methods=["POST"])
def create_env():

    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post("http://proxy/auth/verify", headers=headers)
        if response.status_code != 200:
            return jsonify({"error": "Not authorized"}), 401
    except requests.RequestException:
        return jsonify({"error": "Unable to check token, check /auth API"}), 401
    
    user_data = request.get_json()


    env_url = user_data.get("url", "")
    env_description = user_data.get("description", "")
    env_active = user_data.get("active", True)

    if not "name" in user_data or user_data["name"] == None:
        return jsonify({"error": "name is required"}), 400
    env_name = user_data.get("name")

    if not "type" in user_data or user_data["type"] == None:
        
        return jsonify({"error": "type is required"}), 400
    env_type = user_data.get("type")
        

    envs = load_env()

    env_created_at = datetime.now(timezone.utc).isoformat()
    
    uuid_id = str(uuid.uuid4())

    new_env = {                                                   # On créer un nouvel environnement avec le dernier ID + 1 et les donnée entrée par l'utilisateur
        "id": uuid_id,
        "name": env_name,
        "type": env_type,
        "description": env_description,
        "url": env_url,
        "active": env_active,
        "created_at": env_created_at,
        "updatedAt": env_created_at
    }

    envs[uuid_id] = new_env                                          # On ajoute cet environnement à la fin de liste (qui correspond au fichier)

    save_env(envs)

    return jsonify(new_env), 201

@app.route("/environments", methods=["GET"])
def list_env():

    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post("http://proxy/auth/verify", headers=headers)
        if response.status_code != 200:
            return jsonify({"error": "Not authorized"}), 401
    except requests.RequestException:
        return jsonify({"error": "Unable to check token, check /auth API"}), 401

    envs = load_env()                                              # On charge le fichier des environnements
    return jsonify(envs), 200

@app.route("/environments/<id>", methods=["GET"])
def detail_env(id):

    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post("http://proxy/auth/verify", headers=headers)
        if response.status_code != 200:
            return jsonify({"error": "Not authorized"}), 401
    except requests.RequestException:
        return jsonify({"error": "Unable to check token, check /auth API"}), 401

    envs = load_env()

    env = envs.get(id)

    return jsonify(env), 200

@app.route("/environments/<id>", methods=["PATCH"])
def update_env(id):

    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post("http://proxy/auth/verify", headers=headers)
        if response.status_code != 200:
            return jsonify({"error": "Not authorized"}), 401
    except requests.RequestException:
        return jsonify({"error": "Unable to check token, check /auth API"}), 401

    user_data = request.get_json()

    envs = load_env()

    env = envs.get(id)

    env_updated_at = datetime.now(timezone.utc).isoformat()

    elems = ["name", "description", "type", "url", "active"]

    for elem in elems:
        if elem in user_data:
            env[elem] = user_data[elem]
    env["updatedAt"] = env_updated_at

    envs[id] = env

    save_env(envs)

    return jsonify(envs), 200

@app.route("/environments/<id>", methods=["DELETE"])
def del_env(id):

    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post("http://proxy/auth/verify", headers=headers)
        if response.status_code != 200:
            return jsonify({"error": "Not authorized"}), 401
    except requests.RequestException:
        return jsonify({"error": "Unable to check token, check /auth API"}), 401

    envs = load_env()

    if id in envs :
        del envs[id]
    else : 
        return jsonify({"error":"ID introuvable"}), 400

    save_env(envs)

    return jsonify({"success": True,"message": "Ressource supprimée avec succès","id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"}), 200


if __name__ == '__main__':                                          # On définit les paramètres de notre programme, comme l'adresse qu'il utilise et le port utilisé
    app.run(host="0.0.0.0", port=5002)