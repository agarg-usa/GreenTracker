const React = require("react");
const {
  StyleSheet,
  Button,
  View,
  Text,
  Image,
  ScrollView,
} = require("react-native");

const { DATACONST } = require("./util.js");

function StartScreen({ navigation }) {
  return (
    // <ScrollView>
    <View style={styles.startScreen}>
      <Image
        source={{
          uri: "https://media.discordapp.net/attachments/1032434111006118012/1033626593815437362/logo_1.png",
        }}
        style={{ width: 350, height: 350, margin: 80, borderRadius: 350 }}
      />
      <Text style={styles.startText}>GreenTracker</Text>
      {/* <Text style={styles.sloganText}>Slogan</Text> */}
      <View style={styles.button}>
        <Button
          color="black"
          title="Login"
          onPress={() => {
            navigation.navigate("Login");
          }}
        />
      </View>
      {/* <Text style={styles.description}>In 1891, founding Stanford University president David Starr Jordan influenced Frank Cramer to open the Palo Alto Preparatory School for Boys.[6]</Text> */}
    </View>
    // {/* </ScrollView> */}
  );
}

export { StartScreen };

const styles = StyleSheet.create({
  startScreen: {
    backgroundColor: DATACONST.bkgColorMain,
    justifyContent: "top",
    alignItems: "center",
    flex: 1,
  },
  startText: {
    fontFamily: DATACONST.font,
    fontSize: 50,
    color: DATACONST.fontColor,
    fontWeight: "bold",
    textAlign: "center",
    paddingVertical: 20,
  },
  sloganText: {
    fontFamily: DATACONST.font,
    fontSize: 30,
    color: DATACONST.fontColor,
    fontWeight: "bold",
    textAlign: "center",
  },
  description: {
    fontFamily: DATACONST.font,
    fontSize: 20,
    color: DATACONST.fontColor,
    textAlign: "center",
    paddingVertical: 200,
    margin: 20,
  },
  button: {
    alignItems: "center",
    justifyContent: "center",
    paddingVertical: 10,
    paddingHorizontal: 50,
    borderRadius: 40,
    elevation: 3,
    margin: 10,
    backgroundColor: "black",
  },
});
