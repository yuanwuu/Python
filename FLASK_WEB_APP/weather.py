from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city='new york'):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=imperial'
    weather_data = requests.get(request_url).json()
    return weather_data


if __name__ == "__main__":
    print('\n--- Get Current Weather Conditions ---\n)')
    city = input('\nPlease enter a city name: ')

    # edge cases: empty str.,
    if not bool(city.strip()):  # if it is true, at city input stripe away spaces!
        city = 'New York'

    weather_data = get_current_weather(city)
    print("\n")
    pprint(weather_data)
