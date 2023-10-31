import React, { useState, useEffect } from 'react';
import { View, Text, TextInput, Button, Alert, Pressable } from 'react-native';
import * as Location from 'expo-location';
import MapView, { Marker } from 'react-native-maps';

import tw from 'twrnc'

const App = () => {
  const [movieTitle, setMovieTitle] = useState('');
  const [movieData, setMovieData] = useState(null);

  const [location, setLocation] = useState(null);

  useEffect(() => {
    (async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== 'granted') {
        Alert.alert('Permissão de localização não concedida', 'Por favor, conceda permissão de localização para obter a localização.');
        return;
      }
      let locationData = await Location.getCurrentPositionAsync({});
      setLocation(locationData);
    })();
  }, []);

  const handleSearch = async () => {
    if (movieTitle.trim() === '') {
      Alert.alert('Aviso', 'Por favor, insira um título de filme válido.');
      return;
    }
    try {
      const apiKey = '9cd1d243'; // Substitua pelo seu próprio API Key
      const apiUrl = `https://www.omdbapi.com/?t=${movieTitle}&apikey=${apiKey}`;
      const response = await fetch(apiUrl);
      const data = await response.json();
      if (data.Response === 'True') {
        setMovieData(data);
      } else {
        Alert.alert('Erro', 'Filme não encontrado. Verifique o título e tente novamente.');
      }
    } catch (error) {
      console.error(error);
      Alert.alert('Erro', 'Houve um problema na busca do filme. Tente novamente mais tarde.');
    }
  };

  const mapStyle = [
    {
      "elementType": "geometry",
      "stylers": [
        {
          "color": "#242f3e"
        }
      ]
    },
    {
      "elementType": "labels.text.fill",
      "stylers": [
        {
          "color": "#746855"
        }
      ]
    },
    {
      "elementType": "labels.text.stroke",
      "stylers": [
        {
          "color": "#242f3e"
        }
      ]
    },
    {
      "featureType": "administrative.locality",
      "elementType": "labels.text.fill",
      "stylers": [
        {
          "color": "#d59563"
        }
      ]
    },
    {
      "featureType": "poi",
      "elementType": "labels.text.fill",
      "stylers": [
        {
          "color": "#d59563"
        }
      ]
    },
    {
      "featureType": "poi.park",
      "elementType": "geometry",
      "stylers": [
        {
          "color": "#263c3f"
        }
      ]
    },
    {
      "featureType": "poi.park",
      "elementType": "labels.text.fill",
      "stylers": [
        {
          "color": "#6b9a76"
        }
      ]
    },
    {
      "featureType": "road",
      "elementType": "geometry",
      "stylers": [
        {
          "color": "#38414e"
        }
      ]
    },
    {
      "featureType": "road",
      "elementType": "geometry.stroke",
      "stylers": [
        {
          "color": "#212a37"
        }
      ]
    },
    {
      "featureType": "road",
      "elementType": "labels.text.fill",
      "stylers": [
        {
          "color": "#9ca5b3"
        }
      ]
    },
    {
      "featureType": "road.highway",
      "elementType": "geometry",
      "stylers": [
        {
          "color": "#746855"
        }
      ]
    },
    {
      "featureType": "road.highway",
      "elementType": "geometry.stroke",
      "stylers": [
        {
          "color": "#1f2835"
        }
      ]
    },
    {
      "featureType": "road.highway",
      "elementType": "labels.text.fill",
      "stylers": [
        {
          "color": "#f3d19c"
        }
      ]
    },
    {
      "featureType": "transit",
      "elementType": "geometry",
      "stylers": [
        {
          "color": "#2f3948"
        }
      ]
    },
    {
      "featureType": "transit.station",
      "elementType": "labels.text.fill",
      "stylers": [
        {
          "color": "#d59563"
        }
      ]
    },
    {
      "featureType": "water",
      "elementType": "geometry",
      "stylers": [
        {
          "color": "#17263c"
        }
      ]
    },
    {
      "featureType": "water",
      "elementType": "labels.text.fill",
      "stylers": [
        {
          "color": "#515c6d"
        }
      ]
    },
    {
      "featureType": "water",
      "elementType": "labels.text.stroke",
      "stylers": [
        {
          "color": "#17263c"
        }
      ]
    }
  ]

  return (
    <View style={tw`w-full h-full bg-black p-6 flex items-center justify-start flex-col`}>
      <Text style={tw`text-white mt-10 w-full text-center font-bold text-lg`}>
        Busca de Filmes
      </Text>
      <View style={tw`mt-2 flex items-center justify-center flex-row w-full gap-3`}>
        <TextInput
          style={tw`my-2 p-3 rounded-lg bg-slate-700 text-lg text-white w-3/6`}
          placeholder="Digite o nome do filme"
          value={movieTitle}
          onChangeText={(text) => setMovieTitle(text)}
        />
        <Pressable style={tw`p-4 w-2/6 rounded-lg bg-sky-600`} onPress={handleSearch}>
          <Text style={tw`text-white text-center font-bold`}>Buscar Filme</Text>
        </Pressable>
      </View>

      {movieData && (
        <View style={tw`m-4 p-4 text-white bg-slate-700 rounded-lg w-5/6`}>
          <Text style={tw`text-white font-bold text-lg mb-4`}>Filme Informado:</Text>
          <Text style={tw`text-white font-bold text-lg`}>{movieData.Title}</Text>
          <Text style={tw`text-white my-2`}>Ano: {movieData.Year}</Text>
          <Text style={tw`text-white my-2`}>Gênero: {movieData.Genre}</Text>
          <Text style={tw`text-white my-2`}>Diretor: {movieData.Director}</Text>
          <Text style={tw`text-white my-2`}>Prêmios: {movieData.Awards}</Text>
        </View>
      )}

      {location && (
        <View style={tw`rounded-lg bg-slate-700 p-4 w-5/6`}>
          <Text style={tw`text-white font-bold text-lg mb-4`}>Sua Localização</Text>
          <Text style={tw`text-white mb-2 font-bold`}>Latitude: {location.coords.latitude}</Text>
          <Text style={tw`text-white mb-4 font-bold`}>Longitude: {location.coords.longitude}</Text>
          <View style={{ width: '100%', height: 200, borderRadius: 10, overflow: 'hidden' }}>
            <MapView
              // style={{ width: '100%', height: 200 }}
              style={{ width: '100%', height: 200 }}
              initialRegion={{
                latitude: location.coords.latitude,
                longitude: location.coords.longitude,
                latitudeDelta: 0.0922,
                longitudeDelta: 0.0421,
              }}
              customMapStyle={mapStyle}
            >
              <Marker
                coordinate={{
                  latitude: location.coords.latitude,
                  longitude: location.coords.longitude,
                }}
                title="Sua Localização"
                pinColor="blue"
              />
            </MapView>
          </View>
        </View>
      )}
    </View>
  );
};
export default App;