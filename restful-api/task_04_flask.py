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
    if username not in users:
        return {"error": "User not found"}, 404
    return users[username]


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    name = data.get('name')
    age = data.get('age')
    city = data.get('city')

    if not username:
        return jsonify({'error': 'Username is required'}), 400

    if username in users:
        return jsonify({'error': 'User already exists'}), 400

    users[username] = data

    return jsonify({
        'message': 'User added successfully',
        'user': users[username]
    })


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


if __name__ == '__main__':
    app.run(debug=True)