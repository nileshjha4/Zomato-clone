from src import app
from flask import Flask, render_template, request, make_response, send_file,jsonify
import requests
import json

signupUrl = "https://auth.butane33.hasura-app.io/v1/signup"
loginUrl = "https://auth.butane33.hasura-app.io/v1/login"
dataUrl = "https://data.butane33.hasura-app.io/v1/query"
logoutUrl = "https://auth.butane33.hasura-app.io/v1/user/logout"

headers = {
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    return "Hasura Hello World"

@app.route('/signup/', methods=['POST'])
def zomatoSignup():
    userSignupData = request.get_json()
    signupPayload = {
        "provider": "username",
        "data": {
            "username": userSignupData['username'],
            "password": userSignupData['password']
        }
    }
    try:
        resp = requests.request("POST", signupUrl, data=json.dumps(signupPayload), headers=headers).json()
        print(resp)
        return jsonify({"auth_token" : resp['auth_token']})
    except KeyError:
        return jsonify({"message" : resp['message']})


@app.route('/login/', methods=['POST'])
def zomatoLogin():
    userLoginData = request.get_json()
    loginPayload = {
        "provider": "username",
        "data": {
            "username": userLoginData['username'],
            "password": userLoginData['password']
        }
    }
    try:
        resp = requests.request("POST", loginUrl, data=json.dumps(loginPayload), headers=headers).json()
        print(resp)
        return jsonify({"auth_token" : resp['auth_token']})
    except KeyError:
        return jsonify({"message" : resp['message']})

@app.route('/signout/', methods=['POST'])
def zomatoLogout():
    Authorization = request.headers.get('Authorization')
    headers = {
        "Content-Type": "application/json",
        "Authorization": Authorization
    }
    print(headers)
    resp = requests.request("POST", logoutUrl, headers=headers).json()
    print(resp)
    return jsonify({"message" : resp['message']})


if __name__ == '__main__':
    app.run(threaded = True)


