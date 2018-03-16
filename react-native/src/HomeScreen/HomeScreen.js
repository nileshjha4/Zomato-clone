import React from "react";
import { Statusbar, Alert, View, Image, StyleSheet, ActivityIndicator, ListView } from 'react-native';
import { Container, Header, Title, Left, Icon, Right, Button, Body, Text, Card, CardItem,
 Form, Item, Input } from 'native-base';
import Search from './searchid.js';
import MaterialCommunityIcon from "react-native-vector-icons/MaterialCommunityIcons";
import FeatherIcon from "react-native-vector-icons/Feather";

export default class HomeScreen extends React.Component {
  
  constructor(props){
    super(props);
    this.state = {
		data: [],
	  	searchTextBox : '',
		isSearchPressed: false,
		isLoading: true,
		
	};

    this.trySearch = this.trySearch.bind(this);
	
  }	
  
  trySearch(search) {
    console.log('Making search query');
    let requestOptions = {
      "method": "POST",
      "headers": {
         "Content-Type":"application/json"
      }
    };

    let body = {
      "searchInput": "Kalyan"
    };

    requestOptions["body"] = JSON.stringify(body);
    console.log("Auth Response ---------------------");
  
    try {
      let response = fetch('https://app.butane33.hasura-app.io/search/', requestOptions)
	    .then((response) => response.json())
        .then((responseJson) => {
          let ds = new ListView.DataSource({rowHasChanged: (r1, r2) => r1 !== r2});
          this.setState({
            isLoading: false,
            dataSource: ds.cloneWithRows(responseJson.restaurantList),
          }, function() {
           // do something with new state
          });
        })
	    .catch((error) => {
          console.error(error);
        });
        console.log(response);
        return response; 
    }
    catch(e) {
      console.log("Request Failed: " + e);
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
 
    async componentDidMount() {
	   await this.trySearch();
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
        <Container>
		    <Form>
		      <Item>
		        <Input value={this.state.searchTextbox} onChangeText={this.handleSearchChange} placeholder="Search Here" />
			    <Button transparent onPress={this.handleSearchPressed}>
			      <Icon name="ios-search" />
			    </Button>
		      </Item>
		    </Form>
        <ListView
          dataSource={this.state.dataSource}
          renderSeparator= {this.ListViewItemSeparator}
          renderRow={(rowData) =>
          <Card style={{flex:1, flexDirection: 'row'}}>
		    <CardItem body>
              <Image source = {{ uri: rowData.restaurant_image_url }} style={{width: 100, height: 100}} />
			</CardItem>
			<CardItem>
			  <Text note>{rowData.restaurant_name}</Text>
			</CardItem>
          </Card>
          }
        />
	  </Container>
    );
  }
}

module.export = HomeScreen;