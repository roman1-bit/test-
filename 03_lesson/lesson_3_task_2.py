from Smartphone import Smartphone


smart1 = Smartphone("Samsung", "galaxy 6", "+79277445119")
smart2 = Smartphone("Apple", "iPhone 16 Pro Max", "+79277445118")
smart3 = Smartphone("Xiaomi", "Xiaomi 15", "+79277445117")
smart4 = Smartphone("Poco", "Poco M7 Pro", "+79277445116")
smart5 = Smartphone("Tecno", "Tecno Camon 40", "+79277445115")

catalog = [smart1, smart2, smart3, smart4, smart5]
for smart in catalog:
    print(smart.brand, smart.model, smart.number)