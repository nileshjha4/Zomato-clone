from src import app
from flask import Flask, render_template, request, make_response, send_file
import requests
import json

authUrl = "https://auth.butane33.hasura-app.io/v1/signup"

@app.route("/")
def home():
    return "Hasura Hello World"

@app.route('/signup', methods=['POST'])
def zomatoSignup():
    userData = request.get_json()
    requestPayload = {
        "provider": "username",
        "data": {
            "username": userData['username'],
            "password": userData['username']
        }
    }
    headers = {
    "Content-Type": "application/json"
    }
    resp = requests.request("POST", authUrl, data=json.dumps(requestPayload), headers=headers).json()
    return jsonify({"auth_token" : resp['auth_token']})

if __name__ == '__main__':
    app.run(threaded = True)


