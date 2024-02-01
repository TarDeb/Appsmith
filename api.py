from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
# Dummy user data
users = {
    "admin": generate_password_hash("12345")
}
@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user_pass_hash = users.get(username)
    if user_pass_hash and check_password_hash(user_pass_hash, password):
        return jsonify({"message": "success"}), 200
    else:
        return jsonify({"message": "Invalid credentialsff"}), 200

if __name__ == '__main__':
    app.run(debug=True)
