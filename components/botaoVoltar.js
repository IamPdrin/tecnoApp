import { View, Button } from 'react-native';
import { router } from 'expo-router';

export default function botaoVoltar() {
    const irParaIndex = () => {
        router.back();
    }

    return (
        <View>
            <Button title="Voltar" onPress={irParaIndex}/>
        </View>
    );
}