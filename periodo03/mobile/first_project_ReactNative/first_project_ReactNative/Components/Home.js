import { Link } from "@react-navigation/native";
import { Button, Image, Linking, Text, View } from "react-native";
import tw from 'twrnc'

export default function Home({ navigation }) {
    return (
        <View style={tw`flex items-center p-5`}>
            <Image style={tw`rounded-full w-50 h-50`} source={require("../assets/perfil.jpg")} />
            <Text style={tw`text-black font-bold text-sm m-4 `}>Me chamo Dayvson Lima, e estou me formando em Análise e Desenvolvimento de Sistemas na Faculdade Senac.</Text>
            <View style={tw`flex items-center flex-row m-4 justify-evenly w-full`}>
                <Text style={tw`text-white font-bold my-2 py-2 px-3 bg-blue-500 rounded-lg`} onPress={() => { Linking.openURL('https://github.com/dayvsonlsantos') }}>Github</Text>
                <Text style={tw`text-white font-bold my-2 py-2 px-3 bg-blue-500 rounded-lg`} onPress={() => { Linking.openURL('https://www.linkedin.com/in/dayvsonlimasantos/') }}>Linkedin</Text>
            </View>
            <Button title="Habilidades" onPress={() => navigation.navigate('Habilidades')}>
            </Button>
        </View>
    )
}