""" Develop a Simple API using Python with Flask"""
from flask import Flask, jsonify, request


app = Flask(__name__)


users = {}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/status')
def status():
    return 'OK'


@app.route('/user/<username>')
def profile(username):
    user = users.get(username)
    if not username:
        return {"error": "User not found"}, 404
    else:
        return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'Username is required'}), 400
    if username in users:
        return jsonify({'error': 'User already exists'}), 400
    users[username] = data
    return jsonify({'message': 'User added', 'user': data}), 201


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


if __name__ == '__main__':
    app.run(debug=True)