from src import app
from flask import Flask, render_template, request, make_response, send_file,jsonify
import requests
import json

signupUrl = "https://auth.butane33.hasura-app.io/v1/signup"
loginUrl = "https://auth.butane33.hasura-app.io/v1/login"
dataUrl = "https://data.butane33.hasura-app.io/v1/query"
logoutUrl = "https://auth.butane33.hasura-app.io/v1/user/logout"
userInfoUrl = "https://auth.butane33.hasura-app.io/v1/user/info"
fileUrl = "https://filestore.butane33.hasura-app.io/v1/file"

headers = {
    "Content-Type": "application/json"
}

dataHeaders= {
    "Content-Type": "application/json",
    "Authorization": "Bearer 79f276cd9a8111dbf1e6f10d02b305cc2aeedc8f31f113e7"
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
        signupResp = requests.request("POST", signupUrl, data=json.dumps(signupPayload), headers=headers).json()
        print("hasura_id : ",signupResp['hasura_id'],", hasura_roles : ",signupResp['hasura_roles'])
    except KeyError:
        return jsonify({"message" : signupResp['message']})
    else:
        userDataPayload = {
            "type": "insert",
            "args": {
                "table": "users",
                "objects": [
                    {
                        "hasura_id" : signupResp['hasura_id'],
                        "name" : userSignupData['name'] ,
                        "username" : signupResp['username'] ,
                    }
                ]
                }
            }
        # Make the query and store response in resp
        dataResp = requests.request("POST", dataUrl, data=json.dumps(userDataPayload), headers=dataHeaders).json()
        print(dataResp)
        return jsonify({"auth_token" : signupResp['auth_token']})


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
        loginResp = requests.request("POST", loginUrl, data=json.dumps(loginPayload), headers=headers).json()
        print("hasura_id : ",loginResp['hasura_id'],", hasura_roles : ",loginResp['hasura_roles'])
        return jsonify({"auth_token" : loginResp['auth_token']})
    except KeyError:
        return jsonify({"message" : loginResp['message']})
    

@app.route('/signout/', methods=['POST'])
def zomatoLogout():
    logoutToken = request.get_json()
    Authorization = "Bearer " + logoutToken['auth_token']
    headers = {
        "Content-Type": "application/json",
        "Authorization": Authorization
    }
    print(headers)
    resp = requests.request("POST", logoutUrl, headers=headers).json()
    print(resp)
    return jsonify({"message" : resp['message']})

@app.route('/homefeed/', methods=['POST'])
def homeFeed():
    userLocation = request.get_json()
    loctionPayload = {
        "type": "select",
        "args": {
            "table": "restaurant",
            "columns": [
                "restaurant_id",
                "restaurant_name",
                "restaurant_image_url",
                "state"
            ],
            "where": {
                "$and": [
                    {
                        "$and": [
                            {
                                "latitude": {
                                    "$gt": userLocation['latitude']-0.5
                                }
                            },
                            {
                                "latitude": {
                                    "$lt": userLocation['latitude']+0.5
                                }
                            }
                        ]
                    },
                    {
                        "$and": [
                            {
                                "longitude": {
                                    "$gt": userLocation['longitude']-0.5
                                }
                            },
                            {
                                "longitude": {
                                    "$lt": userLocation['longitude']+0.5
                                }
                            }
                        ]
                    }
                ]
            },
            "order_by": [
                {
                    "column": "restaurant_id",
                    "order": "asc"
                }
            ]
        }
    }
    resturantList = requests.request("POST", url, data=json.dumps(loctionPayload), headers=dataHeaders).json()
    print(restaurantList)
    return jsonify({"message":"ok"})

    


if __name__ == '__main__':
    app.run(threaded = True)

https://filestore.butane33.hasura-app.io/v1/file/e8d5d65c-539d-4caf-9949-cd97bb647698





# This is the json payload for the query
requestPayload = {
    "type": "select",
    "args": {
        "table": "restaurant",
        "columns": [
            "restaurant_id",
            "restaurant_name",
            "restaurant_image_url",
            "state"
        ],
        "where": {
            "$and": [
                {
                    "$and": [
                        {
                            "latitude": {
                                "$gt": "18.0"
                            }
                        },
                        {
                            "latitude": {
                                "$lt": "20.0"
                            }
                        }
                    ]
                },
                {
                    "$and": [
                        {
                            "longitude": {
                                "$gt": "72.0"
                            }
                        },
                        {
                            "longitude": {
                                "$lt": "73.0"
                            }
                        }
                    ]
                }
            ]
        },
        "order_by": [
            {
                "column": "restaurant_id",
                "order": "asc"
            }
        ]
    }
}

# Setting headers
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 79f276cd9a8111dbf1e6f10d02b305cc2aeedc8f31f113e7"
}

# Make the query and store response in resp
resp = requests.request("POST", url, data=json.dumps(requestPayload), headers=headers)

# resp.content contains the json response.
print(resp.content)