#this is a file to get the weather for the day, and for the day after.
#open weather map
import os
import requests
from dotenv import load_dotenv

load_dotenv()

#accesses weather apin key from the .env. 
#declares city and units to use, rather than hardcoding
API_KEY = os.getenv("WEATHER_API_KEY")

CITY = "BELFAST"
UNITS = "metric"


#the api uses co ordinates rather than a city name. As the pi is used in the exact same place, it is hardcoded.
#to change city, google the co-ordinates and change the variables below!

latitude = 54.5970
longitude = -5.9300

#function to fetch the data
def weatherData():
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={latitude}&lon={longitude}&units={UNITS}&appid={API_KEY}"
    )
    print(f"Requesting URL: {url}")  
    response = requests.get(url)
    print(f"Status code: {response.status_code}") 
    data = response.json()
    print(f"JSON response keys: {list(data.keys())}")  
    return data


def currentWeather():
    data = weatherData()

    if "main" not in data or "weather" not in data:
        print("Weather data missing expected keys.")
        return "Weather unavailable"

    currentTemp = round(data["main"]["temp"])
    print(f"Current temperature: {currentTemp}°C")  

    conditions = [w["main"].lower() for w in data["weather"]]
    print(f"Conditions list: {conditions}")  

    willRain = "rain" in conditions
    isRaining = "Rain expected!!!" if willRain else "No rain!"

    print(f"Rain status: {isRaining}")  

    return f"{currentTemp}°C — {isRaining}"

currentWeather()