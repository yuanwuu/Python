import requests  # allows to send HTTP methods request eg. .get
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()


def get_currrent_weather():
    print("\n--- Get Current Weather Condition ---\n")
    city = input('\nPlease enter a city name. \n')

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=imperial'

    # print(request_url)
    weather_data = requests.get(request_url).json()
    # pprint(weather_data) # in organized json format

    print(f"\nCurrent weather for {weather_data["name"]}.")
    print(f"\nThe temp is {weather_data["main"]["temp"]}.")
    print(f"\nFeels like {weather_data["main"]["feels_like"]} and {
          weather_data["weather"][0]["description"]}.\n")


if __name__ == "__main__":
    get_currrent_weather()
