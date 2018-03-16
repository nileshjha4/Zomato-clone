import React from "react";
import { AppRegistry, View, Image } from "react-native";
import { Container, Content, Header, Left, Right, Icon, Button, Text, Card, Thumbnail } from "native-base";
import MaterialCommunityIcon from "react-native-vector-icons/MaterialCommunityIcons";

const clusterName = "butane33"

const loginUrl = "https://app." + clusterName + ".hasura-app.io/login/";
const signupUrl = "https://app." + clusterName + ".hasura-app.io/signup/";
const searchUrl = "https://app." + clusterName + ".hasura-app.io/search/";

import { Alert } from 'react-native';

const networkErrorObj = {
  status: 503
}

export async function trySignup(username, name, password) {
  console.log('Making signup query');
  let requestOptions = {
    "method": "POST",
    "headers": {
      "Content-Type":"application/json"
    }
  };

  let body = {
    "username": username,
    "name": name,
    "password": password
  };

  requestOptions["body"] = JSON.stringify(body);
  console.log("Auth Response ---------------------");
  
  try {
    let resp = await fetch(signupUrl, requestOptions);
    console.log(resp);
    return resp; 
  }
  catch(e) {
    console.log("Request Failed: " + e);
    return networkErrorObj;
  }
}

export async function tryLogin(username, name, password) {
  console.log('Making login query');
  let requestOptions = {
    "method": "POST",
    "headers": {
      "Content-Type":"application/json"
    }
  };

  let body = {
    "username": username,
	"name": name,
    "password": password
  };

  requestOptions["body"] = JSON.stringify(body);

  console.log("Auth Response ---------------------");
  
  try {
    let resp = await fetch(loginUrl, requestOptions);
    console.log(resp);
    return resp; 
  }
  catch(e) {
    console.log("Request Failed: " + e);
    return networkErrorObj;
  }
}

export async function trySearch(search) {
  console.log('Making search query');
  let requestOptions = {
    "method": "POST",
    "headers": {
      "Content-Type":"application/json"
    }
  };

  let body = {
    "searchInput": search
  };

  requestOptions["body"] = JSON.stringify(body);
  console.log("Auth Response ---------------------");
  
  try {
    let resp = await fetch(searchUrl, requestOptions);
    console.log(resp);
    return resp; 
  }
  catch(e) {
    console.log("Request Failed: " + e);
    return networkErrorObj;
  }
}

export default class Startup extends React.Component {
  render() {
	return (
	  <Container>
	    <Content style={{paddingTop:60}}>
		  <Image 
		    style={{alignSelf: "center", width: 300, height: 320}} 
			source={require('./tomato.png')} 
		  />
		  <View style={{flex: 1, flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center'}}>
		    <Card>
            <Button light block style={{backgroundColor: "white"}}
			  onPress={() => this.props.navigation.navigate("Signup")}>
		      <Text style={{textAlign: "center"}}>Login & Sign up</Text>
		    </Button>
		    </Card>
		  </View>
		</Content>
	  </Container>
	)
  }
}