import os
from pprint import pprint

import requests
from dotenv import load_dotenv

# Load api key value from the .env file

load_dotenv()

# get weather function


def get_current_weather(city="Nairobi"):
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
   
    # Get the weather data
    weather_data = requests.get(request_url).json()
    return weather_data


# Main module
if __name__ == "__main__":
       
    print("\n *** Get Current Weather Conditions *** \n")

    city = input("\n Please Enter a City name: ")
    try:
        weather_data = get_current_weather(city)
        print("\n")
        pprint(weather_data)
    except Exception as e:
        print(f"Error: {e}")
