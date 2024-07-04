from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv() # load api key from .env

# Function to get weather data
def get_current_weather(city = "Nairobi"):
    
    request_url = f'http://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    weather_data = requests.get(request_url).json()
    
    return weather_data

# Main Module
if __name__ == '__main__':
    print('\n *** Get Weather Conditions *** \n')
    
    city = input('Please enter a City name: ')
    
    #Check for empty string or string with only spaces
    if not bool(city.strip()): 
        city = "Nairobi"    # deafault city name if no city is entered

    weather_data = get_current_weather(city)
    
    print('\n')    
    pprint(weather_data)