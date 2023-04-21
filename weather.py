import requests
import datetime

# Function to get location coordinates


def get_location_coords(location):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={location}&count=1&language=en&format=json"
    response = requests.get(url).json()
    if len(response) == 0:
        return None
    else:
        # print('location response', response["results"][0])
        res = response["results"][0]
        coords = {
            "latitude": res["latitude"],
            "longitude": res["longitude"],
            "timezone": res["timezone"]
        }
        return coords

# Function to get weather forecast data


def get_weather_forecast(coords):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={coords['latitude']}&longitude={coords['longitude']}&hourly=temperature_2m,precipitation_probability,precipitation&current_weather=true&timezone={coords['timezone']}&temperature_unit=fahrenheit"
    response = requests.get(url).json()
    # print("get weather data", response)
    return response

# Function to print weather forecast


def print_weather_forecast(location, data):
    weather = data['current_weather']
    print(f"Weather forecast for {location, weather}:")
    


# Main program
location = input("Enter location (city, state/province, country): ")
coords = get_location_coords(location)
if coords is None:
    print(f"{location} not found.")
else:
    # print('coords', coords)
    data = get_weather_forecast(coords)
    print_weather_forecast(location, data)
