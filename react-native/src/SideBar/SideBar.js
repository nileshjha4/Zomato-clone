import React from "react";
import { AppRegistry, StatusBar } from "react-native";
import { Container, Content, Header, Thumbnail, Left, Right, Body, Icon, Button, Text, List, ListItem } from "native-base";
import IonIcon from "react-native-vector-icons/Ionicons";
import MaterialCommunityIcon from "react-native-vector-icons/MaterialCommunityIcons";
import OctiIcon from "react-native-vector-icons/Octicons";
import Feather from "react-native-vector-icons/Feather";
import Entypo from "react-native-vector-icons/Entypo";
export default class SideBar extends React.Component {
  render() {
	return (
	  <Container>
	    <Content>
		  <Header style={{backgroundColor: "white"}}>
		    <Text note style={{fontSize: 30}}>zomato</Text>
		  </Header>
		  <List>
		    <ListItem>
			<Left>
			<Thumbnail style={{width: 50, height: 50}} source={require('./react/favicon.png')} />
			<Body>
			  <Text style={{ fontWeight: 'bold' }}>Bipin Jaiswar</Text>
			  <Text note>0 Reviews, 0 Followers</Text>
			</Body>
            </Left>
              <Entypo note name="chevron-small-right" style={{ fontSize: 24}} />
			</ListItem>
		    <ListItem noBorder
			  onPress={() => this.props.navigation.navigate("Profile")}>
              <Feather name="user" style={{ paddingLeft: 12, fontSize: 30, color: "blue"}} />
              <Text style={{ paddingLeft: 10 }}>Profile</Text>
            </ListItem>
			<ListItem noBorder
			  onPress={() => this.props.navigation.navigate("About")}>
              <OctiIcon name="info" style={{ paddingLeft: 14, fontSize: 30, color: "yellow" }} />
              <Text style={{ paddingLeft: 9 }}>About</Text>
            </ListItem>
			<ListItem noBorder
			  onPress={() => this.props.navigation.navigate("Add")}>
              <IonIcon name="md-restaurant" style={{ paddingLeft: 14, fontSize: 30, color: "green" }} />
              <Text style={{ paddingLeft: 14}}>Add restaurant</Text>
            </ListItem>
			<ListItem noBorder
			  onPress={() => this.props.navigation.navigate("Search")}>
              <IonIcon name="md-restaurant" style={{ paddingLeft: 14, fontSize: 30, color: "green" }} />
              <Text style={{ paddingLeft: 14}}>search</Text>
            </ListItem>
			<ListItem noTopBorder>
			  <OctiIcon name="sign-out" style={{ paddingLeft: 14, fontSize: 30 }} />
              <Text style={{ paddingLeft: 10 }}>Sign out</Text>
            </ListItem>
		  </List>
		</Content>
	  </Container> 
	);
  }
}
				  
				