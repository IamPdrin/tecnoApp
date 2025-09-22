import { StatusBar } from 'expo-status-bar';
import { Text, View } from 'react-native';

import Botao from '../components/botaoVoltar';
import Styles from '../styles/style';

export default function Login() {
  return (
    <View style={Styles.container}>
      <Text>Login Screen</Text>
      <Botao />
      <StatusBar style="auto" />
    </View>
  );
}