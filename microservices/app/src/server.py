from src import app
from flask import Flask, render_template, request, make_response, send_file,jsonify
import requests
import json
import geocoder

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


def fetchRestaurantList(latitude, longitude):
    latitudeDown = str(float(userLocation['latitude'])-1.0)
    latitudeUp = str(float(userLocation['latitude'])+1.0)
    longitudeDown = str(float(userLocation['longitude'])-1.0)
    longitudeUp = str(float(userLocation['longitude'])+1.0)
    locationPayload = {
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
                                        "$gt": latitudeDown
                                    }
                                },
                                {
                                    "latitude": {
                                        "$lt": latitudeUp
                                    }
                                }
                            ]
                        },
                        {
                            "$and": [
                                {
                                    "longitude": {
                                        "$gt": longitudeDown
                                    }
                                },
                                {
                                    "longitude": {
                                        "$lt": longitudeUp
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
    restaurantList = requests.request("POST", dataUrl, data=json.dumps(locationPayload), headers=dataHeaders).json()
    print(restaurantList)
    return restaurantList


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
    try:
        userLocation = request.get_json()
        restaurantList = fetchRestaurantList(userLocation['latitude'], userLocation['longitude'])
    except Exception as e:
        print(type(e))
        return jsonify({"message" : "Something went wrong! Try again."})
    if type(restaurantList)==str:
        return jsonify({"message" : "Something went wrong! Try again."})
    return jsonify({"count" : str(len(restaurantList)), "restaurantList" : restaurantList })

    
@app.route('/search/')
def search():
    searchData = request.get_json()
    try:
        searchInput=searchData['searchInput']
    except KeyError :
        return jsonify({"message" : "Search input not recieved"})    
    location = geocoder.google(searchInput)
    if location.latlng==None:
        return jsonify({"message" : "Something went wrong! Try again."})
    restaurantList = fetchRestaurantList(location.lat, location.lng)
    if type(restaurantList)==str:
        return jsonify({"message" : "Something went wrong! Try again."})
    return jsonify({"count" : str(len(restaurantList)), "restaurantList" : restaurantList })



if __name__ == '__main__':
    app.run(threaded = True)




