import { Link } from 'expo-router';

import { StatusBar } from 'expo-status-bar';
import { Text, View } from 'react-native';

import Botao from '../components/botao';
import Styles from '../styles/style';


export default function App() {
  return (
    <View style={Styles.container}>
      <Text style={Styles.cor}>TecnoApp</Text>
      <Botao />
      <StatusBar style="auto" />
    </View>
  );
}


