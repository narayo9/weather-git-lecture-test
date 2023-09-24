import os

import click
import requests

API_KEY = os.getenv("API_KEY")  # OpenWeatherMap API 키를 여기에 넣어주세요.
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',  # 섭씨 단위로 받아옵니다.
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        main_data = data['main']
        weather_data = data['weather'][0]

        city_name = data['name']
        temp = main_data['temp']
        description = weather_data['description']

        return f"{city_name}: {temp}°C, {description}"
    else:
        return f"Error: {data['message']}"

@click.command()
@click.argument('city', required=True)
def main(city):
    """도시 이름을 입력하면 날씨 정보를 가져옵니다."""
    weather_info = get_weather(city)
    click.echo(weather_info)

if __name__ == '__main__':
    main()
