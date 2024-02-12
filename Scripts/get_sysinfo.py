import os, locale, sys, ctypes
import psutil
import urllib.request
import json
import screeninfo

def GetUserLanguage():
	windll = ctypes.windll.kernel32
	UILang = windll.GetUserDefaultUILanguage()
	return locale.windows_locale[UILang]

PythonVersion = sys.version[:4]
Username  = os.getenv('USERNAME')

class battery:
    def percent_as_string():
        battery = psutil.sensors_battery()
        percent = f"{str(battery.percent)}%"
        return f"{percent} plugged" if battery.power_plugged else percent

    def percent_as_number():
        battery = psutil.sensors_battery()
        percent = int(battery.percent)
        return percent

    def is_plugged():
        battery_status = psutil.sensors_battery()
        return True if battery_status.power_plugged else False

def is_net_connection(host="https://www.google.com"):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def get_jsondata(file: str, section: str, position: int, value_section: str):
    with open(file, mode='r') as filesource:
        json_data = json.load(filesource)
        section_json = json_data[section]
        return section_json[position-1][value_section]
