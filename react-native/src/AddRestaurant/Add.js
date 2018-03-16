import React from "react";
import { AppRegistry, Alert, View, StyleSheet } from "react-native";
import { Container, Header, Left, Body, Title, Card, CardItem, Content, Right, Icon, Button, Text } from "native-base";
import { StackNavigator } from "react-navigation";
export default class Profile extends React.Component {
  componentDidMount() {
	Alert.alert("Feature will be Available soon.");
  }
  render() {
	return (
	  <Container>
	    <Content padder>
		  <Card>
		    <CardItem>
			  <Text>Feature not available yet.</Text>
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
          <Icon name="md-arrow-back" />
        </Button>
	  </Left>
	  <Body>
	    <Title>Add Restaurant</Title>
	  </Body>
	  <Right />
	</Header>
  )
});

const styles = StyleSheet.create({
  butt: {
    borderRadius: 50,
	width: 50,
	height: 50,
	position: 'absolute',
	bottom: 20,
	right: 20
  }
});
	
		