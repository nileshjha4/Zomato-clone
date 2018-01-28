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
    try:
        latitudeDown = str(float(latitude)-1.0)
        latitudeUp = str(float(latitude)+1.0)
        longitudeDown = str(float(longitude)-1.0)
        longitudeUp = str(float(longitude)+1.0)
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
    except Exception as e:
        print(type(e))
        return "Something went wrong at the server! Please try again"
    return restaurantList


def getRestaurantDetails(restaurant_id):
    try:    
        restaurantPayload = {
                "type": "select",
                "args": {
                    "table": "restaurant",
                    "columns": [
                        "restaurant_id",
                        "restaurant_name",
                        "address",
                        "pincode",
                        "state",
                        "country",
                        "restaurant_image_url"
                    ],
                    "where": {
                        "restaurant_id": {
                            "$eq": restaurant_id
                        }
                    }
                }
            }
        restaurantData = requests.request("POST", dataUrl, data=json.dumps(restaurantPayload), headers=dataHeaders).json()
        print(restaurantData)
    except Exception as e:
        print(type(e))
        print(e)
        return "Something went wrong at server! Please try again."
    return restaurantData


def getRestaurantReviews(restaurant_id):
    try:    
        restaurantReviewPayload = {
                "type": "select",
                "args": {
                    "table": "review",
                    "columns": [
                        "user_id",
                        "restaurant_id",
                        "rating_stars",
                        "review_text",
                        "created"
                    ],
                    "where": {
                        "restaurant_id": {
                            "$eq": restaurant_id
                        }
                    },
                    "order_by": [
                        {
                            "column": "rating_stars",
                            "order": "asc"
                        }
                    ]
                }
            }
        reviewList = requests.request("POST", dataUrl, data=json.dumps(restaurantReviewPayload), headers=dataHeaders).json()
        print(reviewList)
    except Exception as e:
        print(type(e))
        print(e)
        return "Something went wrong at the server! Try again."
    return reviewList


def getCuisine(restaurant_id):
    try:
        cuisinePayload = {
                "type": "select",
                "args": {
                    "table": "cuisine",
                    "columns": [
                        "restaurant_id",
                        "cuisine_name"
                    ],
                    "where": {
                        "restaurant_id": {
                            "$eq": "4"
                        }
                    }
                }
            }
        cuisineList = requests.request("POST", dataUrl, data=json.dumps(cuisinePayload), headers=dataHeaders).json()
        print(cuisineList)
    except Exception as e :
        print(type(e))
        print(e)
        return "Something went wrong at the server! Please try again."
    return cuisineList


def getRestaurantView(restaurant_id):
    try:
        restaurantViewPayload = {
                "type": "select",
                "args": {
                    "table": "restaurant_view",
                    "columns": [
                        "restaurant_id",
                        "view_image_url"
                    ],
                    "where": {
                        "restaurant_id": {
                            "$eq": restaurant_id
                        }
                    }
                }
            }
        restaurantViewList = requests.request("POST", dataUrl, data=json.dumps(restaurantViewPayload), headers=dataHeaders).json()
        print(restaurantViewList)
    except Exception as e :
        print(type(e))
        print(e)
        return "Something went wrong at the server! Please try again."
    return restaurantViewList


def getRestaurantMenu(restaurant_id):
    try:
        restaurantMenuPayload = {
                "type": "select",
                "args": {
                    "table": "menu",
                    "columns": [
                        "restaurant_id",
                        "menu_url"
                    ],
                    "where": {
                        "restaurant_id": {
                            "$eq": restaurant_id
                        }
                    }
                }
            }
        restaurantMenuList = requests.request("POST", dataUrl, data=json.dumps(restaurantMenuPayload), headers=dataHeaders).json()
        print(restaurantMenuList)
    except Exception as e :
        print(type(e))
        print(e)
        return "Something went wrong at the server! Please try again."
    return restaurantMenuList


def getUserReviews(user_id):
    try:    
        userReviewPayload = {
                "type": "select",
                "args": {
                    "table": "review",
                    "columns": [
                        "user_id",
                        "restaurant_id",
                        "rating_stars",
                        "review_text",
                        "created"
                    ],
                    "where": {
                        "user_id": {
                            "$eq": user_id
                        }
                    },
                    "order_by": [
                        {
                            "column": "rating_stars",
                            "order": "asc"
                        }
                    ]
                }
            }
        reviewList = requests.request("POST", dataUrl, data=json.dumps(userReviewPayload), headers=dataHeaders).json()
        print(reviewList)
    except Exception as e:
        print(type(e))
        print(e)
        return "Something went wrong at the server! Try again."
    return reviewList


def getUserData(user_id):
    try:
        userDataPayload = {
                "type": "select",
                "args": {
                    "table": "users",
                    "columns": [
                        "hasura_id",
                        "name",
                        "username",
                        "photo_url"
                    ],
                    "where": {
                        "hasura_id": {
                            "$eq": user_id
                        }
                    }
                }
            }
        userData = requests.request("POST", url, data=json.dumps(userDataPayload), headers=dataHeaders).json()
        print(userData)
    except Exception as e:
        print(type(e))
        print(e)
        return "Something went wrong at the server! Try again."
    return userData


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
    try:
        restaurantList = fetchRestaurantList(userLocation['latitude'], userLocation['longitude'])
    except KeyError:
        return jsonify({"message" : "Location not recieved"})
    if type(restaurantList)==str:
        return jsonify({"message" : "Something went wrong! Try again."})
    return jsonify({"count" : str(len(restaurantList)), "restaurantList" : restaurantList })

    
@app.route('/search/', methods=['POST'])
def search():
    searchData = request.get_json()
    try:
        searchInput=searchData['searchInput']
    except KeyError :
        return jsonify({"message" : "Search input not recieved"})    
    location = geocoder.google(searchInput)
    if location.latlng==None:
        return jsonify({"message" : "Something went wrong at server! Try again."})
    restaurantList = fetchRestaurantList(location.lat, location.lng)
    if type(restaurantList)==str:
        return jsonify({"message" : "Something went wrong at the server! Try again."})
    return jsonify({"count" : str(len(restaurantList)), "restaurantList" : restaurantList })


@app.route('/getrestaurant/', methods=['POST'])
def getRestaurant():
    restaurantInput = request.get_json()
    try:
        restaurant_id = str(int(restaurantInput['restaurant_id']))
    except KeyError :
        return jsonify({"message" : "Inappropriate request! Try again."})
    except ValueError :
        return     jsonify({"message" : "Invalid restaurant id."})
    restaurantData = getRestaurantDetails(restaurant_id)
    reviewList = getRestaurantReviews(restaurant_id)
    cuisineList = getCuisine(restaurant_id)
    restaurantViewList = getRestaurantView(restaurant_id)
    restaurantMenuList = getRestaurantMenu(restaurant_id)
    if type(restaurantData or reviewList or cuisineList or restaurantViewList or restaurantMenuList)==str:
        return jsonify({"message" : "Something went wrong at the server! Try again."})
    return jsonify({"restaurant_details" : restaurantData , "reviews_count" : str(len(reviewList)), "reviews" : reviewList, "menu_count" :  str(len(restaurantMenuList)), "menu" : restaurantMenuList, "restaurant_view_count" : str(len(restaurantViewList)), "restaurant_view" : restaurantViewList, "cuisine_count" : str(len(cuisineList)), "cuisine" : cuisineList })


@app.route('/getuser/', methods=['POST'])
def getUser():
    userInput = request.get_json()
    try:
        user_id = str(int(userInput['user_id']))
    except KeyError :
        return jsonify({"message" : "Inappropriate request! Try again."})
    except ValueError :
        return jsonify({"message" : "Invalid restaurant id."})
    userData = getUserData(user_id)
    reviewList = getUserReviews(user_id)
    if type(userData or reviewList)==str:
        return jsonify({"message" : "Something went wrong at the server! Try again."})
    return jsonify({"userDetails" : userData, "reviews_count" : str(len(userData)), "reviews" : reviewList})


if __name__ == '__main__':
    app.run(threaded = True)