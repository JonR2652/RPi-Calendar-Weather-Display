from notion_client import Client #imports client class
from datetime import datetime, timedelta #imports python module for times / dates
import os #to interact with the OS, lets us read environment variables ie notion token

from dotenv import load_dotenv  #loads secrets to environment variables

load_dotenv() #loads variables from env into os.environ
NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")

#goes to our calendar (database), queries and returns the event of the day. Could display temp and time too!
notion = Client(auth=NOTION_TOKEN) #initialises Notion API with our token. All calls use this


def todaysEvents():

    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)

#following block uses notionAPI to query the database. "notion.databases.query" makes a POST request. 
#the next line tells the api where to target from the env file.
#the "filter" lines ensure we ony get todays activites, by only querying where the date is >= to today and <tomorrow. A fail-safe rather than just
#saying = today.
#"isoformat" formats the date to be more readable, ie 2025-06-19


    response = notion.databases.query(
        database_id=DATABASE_ID,
        filter={
            "and": [
                {
                    "property": "Date",
                    "date": {"on_or_after": today.isoformat()}
                },
                {
                    "property": "Date",
                    "date": {"before": tomorrow.isoformat()}
                }
            ]
        }
    )

    events = []
    for result in response["results"]:
        props = result["properties"]
        title = props["Name"]["title"][0]["plain_text"] if props["Name"]["title"] else "Untitled"
        date = props["Date"]["date"]["start"]
        time_str = datetime.fromisoformat(date).strftime("%H:%M")
        events.append(f"{time_str} → {title}")
    print(events)        
    return events


todaysEvents()