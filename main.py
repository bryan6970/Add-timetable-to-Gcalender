# Only god will understand this code

from gcsa.event import Event
from gcsa.google_calendar import GoogleCalendar
from gcsa.recurrence import Recurrence, DAILY, WEEKLY
from beautiful_date import *
from PIL import Image
import pytesseract

import pandas as pd
from datetime import date, datetime, timedelta

# import datetime
start_date = 1 / Jun / 2024
end_date = 24 / Jun / 2024

data = {
    MO: {"start_time": (6, 20), "end_time": (14, 30)},
    TU: {"start_time": (6, 20), "end_time": (14, 30)},
    WE: {"start_time": (6, 20), "end_time": (14, 30)},
    TH: {"start_time": (6, 20), "end_time": (14, 30)},
    FR: {"start_time": (6, 20), "end_time": (14, 30)},
}

start_time = 6, 20
end_time = 14, 30

occurences = len([i for i in drange(start_date, end_date, 2 * weeks)])

color_id = "8"


calendar = GoogleCalendar(
    credentials_path="client_secret_325430622350-ct06s30iaa729c0c9jnovihbuerh1sfm.apps.googleusercontent.com.json")

events = []

for day, times in data.items():
    start = start_date[times["start_time"][0]:times["start_time"][1]]
    end = start_date[times["end_time"][0]:times["end_time"][1]]

    event = Event(
        'School',
        start=start + day,
        end=end + day,
        recurrence=[Recurrence.rule(freq=WEEKLY, interval=2, count=occurences)
                    ],
        color_id=color_id

    )
    events.append(calendar.add_event(event))

if input("Enter \"SAVE\" to save the calendar") == "SAVE":
    pass
else:
    print("Deleting events...")
    for event in events:
        calendar.delete_event(event)

