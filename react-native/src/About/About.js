import React from "react";
import { AppRegistry, Alert } from "react-native";
import { Container, Header, Left, Body, Title, Card, CardItem, Content, Right, Icon, Button, Text } from "native-base";
import { StackNavigator } from "react-navigation";
export default class Profile extends React.Component {
  componentDidMount() {
	Alert.alert("Coming Soon.");
  }
  render() {
	return (
	  <Container>
	    <Content padder>
		  <Card>
		    <CardItem>
			  <Left>
			    <Text>About</Text>
			  </Left>
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
	    <Title>About</Title>
	  </Body>
	  <Right />
	</Header>
  )
});
	
		