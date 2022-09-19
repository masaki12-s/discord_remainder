from inspect import getcallargs
import os
import caldav
import datetime
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('url')
username = os.getenv('user')
password = os.getenv('password')

def getCalendar(url=url, username=username, password=password):
    client = caldav.DAVClient(url=url, username=username, password=password)
    principal = client.principal()
    calendars = principal.calendars()
    return calendars

def getevent(days=1):
    today = datetime.datetime.now()
    schedules = []
    calendars = getCalendar()

    for calendar in calendars:
            try:
                events = calendar.date_search(start=today, end=today+datetime.timedelta(days=days), expand=True)
                for event in events:
                    d = {}
                    for event_data in event.data.splitlines():
                        pair = event_data.split(":")
                        d[pair[0]] = pair[1]
                    schedules.append(d)
            except:
                continue
    return schedules

def a(schedules: list):
    for schedule in schedules:

    # d = {}
    # for schedule in schedules:
    #     if 'SUMMARY' in schedule.keys():
    #         key = schedule['SUMMARY']
    #     if 'DTSTART' in schedule.keys():
    #         value1 = schedule['DTSTART'][:8]
    #     elif 'DTSTART;VALUE=DATE' in schedule.keys():
    #         value1 = schedule['DTSTART;VALUE=DATE'][:8]
        
    #     if 'DTEND' in schedule.keys():
    #         value2 = schedule['DTSTART'][:8]
    #     elif 'DTEND;VALUE=DATE' in schedule.keys():
    #         value2 = schedule['DTEND;VALUE=DATE'][:8]
    #     d[key] = (value1,value2)
    # print(d)

print(getevent())