import time
import requests
city = input("\nEnter a city name: ")


def get_weather(city):
    url = f"http://wttr.in/{city}?format=3"
    response = requests.get(url)  # search how request is connected with import

    if response.status_code == 200:
        print(f'\nWeather in {response.text}')
    else:
        print("City not found")


def get_time(city):
    url = f"http://wttr.in/{city}?format=%T"
    response = requests.get(url)

    if response.status_code == 200:  # timeframe to get an answer from the server
        print(f'Current time {city.replace(city, "")}{response.text}:\n')
    else:
        print("City not found")


if __name__ == "__main__":  # fundamental line to prevent the code running
    # byitself if connected to other codes, can often be easily removed
    get_weather(city)  # search why get results at the end
    get_time(city)
