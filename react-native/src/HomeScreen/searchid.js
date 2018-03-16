import React from "react";
import { Statusbar, Alert, View, Image, StyleSheet, ActivityIndicator, ListView, ScrollView } from 'react-native';
import { Container, Header, Title, Left, Icon, Right, Button, Body, Text, Card, CardItem,
 Form, Item, Input, Badge } from 'native-base';
import { trySearch } from '../Login/Startup';
import MaterialCommunityIcon from "react-native-vector-icons/MaterialCommunityIcons";
import FeatherIcon from "react-native-vector-icons/Feather";

export default class RestaurantProfile extends React.Component {
  
  constructor(props){
    super(props);
    this.state = {
		data: [],
	  	searchTextBox : '',
		isLoading: true
	  }
  }	
  
  handleSearchPressed = async () => {
    let resp = await trySearch(this.state.searchTextBox);
    if(resp.status !== 200){
      if (resp.status === 504) {
        Alert.alert("Network Error", "Check your internet connection" )
      } else {
        Alert.alert("Error", "Unauthorized, Invalid username or password")      
      }
    } else {
      this.setState({isLoggedIn:true})  
    }
  }
  
  handleSearchChange = searchTextBox => {
  	this.setState({
  		...this.state,
  		searchTextBox: searchTextBox
  	})
  }
  
  ListViewItemSeparator = () => {
   return (
     <View
       style={{
         height: .5,
         width: "100%",
         backgroundColor: "#000",
       }}
     />
   );
 }
 
componentDidMount() {
  fetch('https://app.butane33.hasura-app.io/getrestaurant/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
	  "restaurant_id": 4
	  })
  })
   .then((response) => response.json())
   .then((responseJson) => {
     let ds = new ListView.DataSource({rowHasChanged: (r1, r2) => r1 !== r2});
     this.setState({
        isLoading: false,
        dataSource: ds.cloneWithRows(responseJson.restaurant),
     }, function() {
          // do something with new state
     });
    })
    .catch((error) => {
      console.error(error);
    });
} 
  
  render() {
    if (this.state.isLoading) {
      return (
        <View style={{flex: 1, paddingTop: 20}}>
          <ActivityIndicator />
        </View>
      );
    }
	
	
  return (
    <View>
      <ListView
        dataSource={this.state.dataSource}
        renderSeparator= {this.ListViewItemSeparator}
        renderRow={(rowData) =>
	    <View style={{flex:1, flexDirection: 'column'}}>
		  <Card style={{justifyContent: 'center',alignItems: 'center',}}>
		    <CardItem style={{flex:1, flexDirection: 'column'}}>{rowData.restaurant_details.map(r => <Image source={{ uri: r.restaurant_image_url }} style={{width:350, height:350}} /> )}</CardItem>
		    <Body>
			  <CardItem>{rowData.restaurant_details.map(r => <Text>Name: {r.restaurant_name}</Text> )}</CardItem>
		      <CardItem>{rowData.restaurant_details.map(r => <Text style={{fontSize:12,color: "grey"}}>{r.state}, {r.country}</Text> )}</CardItem>
		    </Body>
		  </Card>
		  <Text>Menu:</Text>
		  <ScrollView horizontal>{rowData.menu.map(r => <Image source={{ uri: r.menu_url }} style={{width:400, height:350}} /> )}</ScrollView> 
		  <Text>Photos:</Text>
		  <ScrollView horizontal>{rowData.restaurant_view.map(r => <Image source={{ uri: r.view_image_url }} style={{width:250, height:250}} /> )}</ScrollView>
		  <Card>
		    <CardItem>
		      <Text note>Cuisines</Text>
			</CardItem>
		    <CardItem>{rowData.cuisine.map(r => <Text>⬤{r.cuisine_name} </Text> )}</CardItem> 
		  </Card>
		  <Card>
		    <CardItem>
			  <Text style={{fontWeight: 'bold'}}>Address</Text>
			</CardItem>
			<CardItem>
			  <Text>{rowData.restaurant_details.map(r => <Text>{r.address}</Text> )}</Text>
			</CardItem>
		  </Card>
	      <Card>
		    <Header style={{flex: 1, flexDirection: 'row'}}>
			  <Badge success>
                <Text>{rowData.reviews.map(r => <Text>{r.rating_stars}</Text> )}</Text>
              </Badge>
		      <Text>Rating</Text>
			</Header>
			<Text note>WHAT PEOPLE SAY?</Text>
			<CardItem style={{flex:1, flexDirection: 'column'}}>{rowData.reviews.map(r => <Text>{r.created}:,{r.review_text}</Text> )}</CardItem>
		  </Card>
        </View>
          }
      />
	</View>
  );
  }
}
