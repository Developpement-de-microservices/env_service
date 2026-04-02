import os, requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime, timezone
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)

client = MongoClient(os.environ["MONGO_URI"])
db = client.env_db
env_col = db.env

def authentification():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.post("http://proxy/auth/verify", headers=headers)
        if response.status_code != 200:
            return jsonify({"error": "Not authorized"}), 401
    except requests.RequestException:
        return jsonify({"error": "Unable to check token, check /auth API"}), 401


@app.route("/environments/health", methods=["GET"])
def heath_env():
    return jsonify({"status": "ok","service": "Environnements","timestamp": datetime.now(timezone.utc).isoformat()}), 200

@app.route("/environments", methods=["POST"])
def create_env():

    auth_check = authentification()
    if auth_check: 
        return auth_check
    
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

    env_created_at = datetime.now(timezone.utc).isoformat()


    new_env = {
        "name": env_name,
        "type": env_type,
        "description": env_description,
        "url": env_url,
        "active": env_active,
        "createdAt": env_created_at,
        "updatedAt": env_created_at
    }

    result = env_col.insert_one(new_env)
    new_env["id"] = str(result.inserted_id)
    del new_env["_id"]

    return jsonify(new_env), 201

@app.route("/environments", methods=["GET"])
def list_env():

    auth_check = authentification()
    if auth_check: 
        return auth_check
    
    is_empty = env_col.find_one()

    if is_empty is None:
        return jsonify({"error":"La collection est vide"}), 400 

    envs = []
    for env in env_col.find():
        env["id"] = str(env["_id"]) #transforme en id de l'objet mongo
        del env["_id"]
        envs.append(env)

    #envs = env_col.find()


    return jsonify(envs), 200

@app.route("/environments/<id>", methods=["GET"])
def detail_env(id):

    auth_check = authentification()
    if auth_check: 
        return auth_check

    try:
        env = env_col.find_one({"_id": ObjectId(id)}) #conversion en type mongoDB pour son ID
    except:
        return jsonify({"message": "Invalid event ID format"}), 400

    if env:
        env["id"] = str(env["_id"])
        #del env["_id"]
        return jsonify(env), 200
    
    return jsonify({"message": "Environement not found"}), 404

@app.route("/environments/<id>", methods=["PATCH"])
def update_env(id):

    auth_check = authentification()
    if auth_check: 
        return auth_check

    user_data = request.get_json()

    user_data["updatedAt"] = datetime.now(timezone.utc).isoformat()

    env = env_col.find_one({"_id": id})

    if not env:
        return jsonify({"error":"Aucun environnement correspondant pour cet ID"}), 400

    env_col.update_one({"id": id}, {"$set": user_data})


    return jsonify(env_col.find_one({"id": id})), 200

@app.route("/environments/<id>", methods=["DELETE"])
def del_env(id):

    auth_check = authentification()
    if auth_check: 
        return auth_check

    env = env_col.find_one({"id": id})

    if not env:
        return jsonify({"error":"Aucun environnement correspondant pour cet ID"}), 400

    env_col.delete_one({"id": id})

    return jsonify({"success": True,"message": "Ressource supprimée avec succès","id": id}), 200


if __name__ == '__main__':                                          # On définit les paramètres de notre programme, comme l'adresse qu'il utilise et le port utilisé
    app.run(host="0.0.0.0", port=5002)