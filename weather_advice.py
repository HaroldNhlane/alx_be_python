sunny = "Wear a t-shirt and sunglasses."
rainy = "Don't forget your umbrella and a raincoat."
cold = "Make sure to wear a warm coat and a scarf."

weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

if weather == "sunny": 
    print(sunny)

elif weather == "rainy":
    print(rainy)

elif weather == "cold":
    print(cold)

else:
    print("Sorry, I don't have recommendations for this weather.")