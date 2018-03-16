import React from "react";
import { AppRegistry, Alert } from "react-native";
import { Container, Header, Left, Body, Title, Card, CardItem, Content, Right, Icon, Button, Text } from "native-base";
import { StackNavigator } from "react-navigation";
export default class Profile extends React.Component {
  componentDidMount() {
	Alert.alert("No users yet", "Coming Soon");
  }
  render() {
	return (
	  <Container>
	    <Content padder>
		  <Card>
		    <CardItem>
			  <Icon active name="paper-plane" />
			  <Text>Profiles</Text>
			  <Right>
			    <Icon name="close" />
			  </Right>
			</CardItem>
		  </Card>
		</Content>
	  </Container>
	);
  }
}

Profile.navigationOptions = ({ navigation }) => ({
  header: (
    <Header>
      <Left>
        <Button transparent onPress={() => navigation.navigate("DrawerOpen")}>
          <Icon name="menu" />
        </Button>
	  </Left>
	  <Body>
	    <Title>Profile</Title>
	  </Body>
	  <Right />
	</Header>
  )
});
	
		