from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from controllers import UserController

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return jsonify({"message": "Welcome to the Connectify backend!"})

@app.route('/users')
def get_users():
    users = UserController.get_all_users()
    user_list=[]
    for user in users:
        user_list.append(format_users(user))
    return jsonify(user_list)

def format_users(user):
    return {
        "id": user[0],
        "username": user[1],
        "password": user[2]
    }

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    UserController.register_user(username, password)
    return jsonify({"username":username, "password":password})


