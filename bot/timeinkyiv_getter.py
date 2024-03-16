import requests


def get_time():
    time = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=Europe/Kyiv").json()
    return {
        "h": "{:02d}".format(time["hour"]),
        "m": "{:02d}".format(time["minute"]),
        "s": "{:02d}".format(time["seconds"]),
    }
