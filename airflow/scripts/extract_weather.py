import requests
import json
import os

API_KEY ="cca7d850b0fde0df2f8c3bf76dfc777e"
cities = ["Hanoi", "Ho Chi Minh", "Da Nang"]

def get_weather(city):
 try:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},VN&appid={API_KEY}&units=metric"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()
 except Exception as e:
        print(f"Error getting weather for {city}: {str(e)}")
        return None

def main():
    data = []
    for city in cities:
        weather = get_weather(city)
        data.append(weather)
    
    with open("/tmp/weather_raw.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    main()