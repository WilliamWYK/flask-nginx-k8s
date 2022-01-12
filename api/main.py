#main.py
from flask import Flask, jsonify, request
from db import get_users, add_user

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello world"

@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == 'POST':
        user = request.get_json(force=True)
        add_user(user)
        return 'User added'
    return get_users()

if __name__ == '__main__':
    app.run()
