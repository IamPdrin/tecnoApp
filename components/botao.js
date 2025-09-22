import { View, Button } from 'react-native';
import { router } from 'expo-router';

export default function botao() {

    const irParaLogin = () => {
        router.push('/login');
    };

    return (
        <View>
            <Button title="Login" onPress={irParaLogin}/>
        </View>
    );
}