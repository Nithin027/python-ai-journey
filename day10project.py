import requests

def get_weather(city):
    api_key = "29df5f40ccfefb18ef97236d774342dd"
    url = f"https://wttr.in/{city}?formart=j1"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['current_condition'][0]['temp_C']
        feels_like = data['current_condition'][0]['FeelslikeC']
        description = data['current_condition'][0]['weatherDesc'][0]['value'] 

        print(f"City: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Feels like: {feels_like}°C")
        print(f"Condition: [{description}]")

    else:
        print(f"Error code: {response.status_code}")
        print(response.json())


get_weather("London")
get_weather("Colorado")
              