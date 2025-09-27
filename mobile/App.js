import React, { useEffect, useState } from "react";
import { SafeAreaView, Text, FlatList, View, TouchableOpacity } from "react-native";

export default function App() {
  const [shops, setShops] = useState([]);

  useEffect(() => {
    fetch("https://YOUR-RAILWAY-URL.up.railway.app/api/shops")
      .then(res => res.json())
      .then(data => setShops(data));
  }, []);

  return (
    <SafeAreaView style={{ flex: 1, padding: 20 }}>
      <Text style={{ fontSize: 24, fontWeight: "bold" }}>DámdyBox 🛒</Text>
      <FlatList
        data={shops}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={{ padding: 15, marginVertical: 10, backgroundColor: "#f5f5f5", borderRadius: 10 }}>
            <Text style={{ fontSize: 18 }}>{item.name}</Text>
            <Text>Скидка: {item.discount}%</Text>
            <Text>Закрытие: {item.closing}</Text>
            <TouchableOpacity style={{ marginTop: 10, backgroundColor: "green", padding: 10, borderRadius: 5 }}>
              <Text style={{ color: "white" }}>Посмотреть</Text>
            </TouchableOpacity>
          </View>
        )}
      />
    </SafeAreaView>
  );
}
