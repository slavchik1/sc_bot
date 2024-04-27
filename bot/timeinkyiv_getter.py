from datetime import datetime
from datetime import timezone
import pytz


def get_time():
    time = datetime.now(timezone.utc).astimezone(pytz.timezone("Europe/Kyiv"))
    return {
        "h": "{:02d}".format(time.hour),
        "m": "{:02d}".format(time.minute),
        "s": "{:02d}".format(time.second)
    }

def get_day():
    return datetime.now(timezone.utc).astimezone(pytz.timezone("Europe/Kyiv")).day
