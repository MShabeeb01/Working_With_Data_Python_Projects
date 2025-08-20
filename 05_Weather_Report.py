# Weather app using OpenWeatherMap API (Application Programming Interface)
import requests

# Step-1: API Setup
API_KEY = "caad385c2c986b9f591e855c93a002f8"   # replace with your own key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# Step-2: Get Weather Data
def get_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = {
                "City": data["name"],
                "Temperature": f"{data['main']['temp']} °C",
                "Weather": data["weather"][0]['description'].title(),
                "Humidity": f"{data['main']['humidity']}%",
                "Wind Speed": f"{data['wind']['speed']} m/s"
            }
            return weather

        elif response.status_code == 404:
            print("City not found.")
        else:
            print("An error occurred. Status code:", response.status_code)

    except Exception as e:
        print("An error occurred:", e)

    return None


# Step-3: Display weather information
def display_weather(weather):
    print("\n--- Weather Information ---")
    for key, value in weather.items():
        print(f"{key}: {value}")


# Step-4: Main program loop
while True:
    print("\n--- Weather App ---")
    city = input("Enter a city name (or 'q' to quit): ").strip()
    if city.lower() == 'q':
        break

    weather = get_weather(city)
    if weather:
        display_weather(weather)
