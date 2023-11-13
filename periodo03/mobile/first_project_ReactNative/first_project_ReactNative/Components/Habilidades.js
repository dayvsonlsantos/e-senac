import { Button, Image, SafeAreaView, SectionList, Text, View } from "react-native";
import tw from 'twrnc'

const data = [
    {
        title: 'Habilidades',
        data: [
            'HTML',
            'CSS',
            'Tailwinds',
            'Bootstrap',
            'React.js',
            'Next.js',
            'Node.js',
            'Python',
            'MySQL',
            'MongoDB',
            'PostgreSQL',
            'Scrum',
            'Kanbam',
            'Git / Github',
            'Docker',
            'Figma',
        ],
    },
];

export default function Habilidades({ navigation }) {
    return (
        <View style={tw`flex items-center p-5`}>
            <SafeAreaView style={tw`flex items-center`}>
                <SectionList
                    sections={data}
                    keyExtractor={(item) => item}
                    renderItem={({ item }) => (
                        <View style={tw`flex items-center m-2`}>
                            <Text style={tw`flex items-center`}>{item}</Text>
                        </View>
                    )}
                    renderSectionHeader={({ section: { title } }) => (
                        <Text style={tw`font-bold m-2 text-lg`}>{title}</Text>
                    )}
                />
            </SafeAreaView>
            <Button title="Home" onPress={() => navigation.navigate('Home')}>
            </Button>
        </View>
    )
}