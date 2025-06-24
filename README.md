Raspberry Pi Zero 2w Weather/Calendar E-Ink Display

This project is a python based dashboard for the raspberry pi zero 2w and the Waveshare 2.13" E-ink Screen.
This project uses the NotionAPI to grab the events for the day, as well as OpenWeatherMap's API to grab the current temperature and rain status.
As a note, to change the location of the weather display, change the "longitude" and "latitude" variables in the "weatherScript.py".
This project also requires the use of a ".env" file, containing the API keys;

NOTION_TOKEN=your_secret_notion_token
NOTION_DATABASE_ID=your_calendar_database_id
WEATHER_API_KEY=your_weather_api_key



##FEATURES##

-Displays current date and time
-Fetches todays events from a Notion calendar database
-Displays current temperature / rain status
-Updates once per minute to keep the time relevant, and a fallback once per hour for the temperature


##DEPENDENCIES##
-Raspberry Pi Zero 2w
-Waveshare 2.13" v4 e-Paper display
Libraries;
  -Python3
  -PIP
  -requests
  -Pillow
  -waveshare_epd
  -dotenv
  -gpiozero OR RPi.GPIO (dependant on driver config)
  -Enabling SPI in raspiconfig

  It is recommended to use a virtual environment for these to avoid conflictions with other projects. There is a script named setup.sh to help to install these! 
