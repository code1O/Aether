import json
import screeninfo
from .get_sysinfo import (
    get_jsondata, GetUserLanguage, Username
)

def writejson(file, section, position, value_section, newvalue_section):
    with open(file, mode="r+") as jsonfile:
        data = json.load(jsonfile)
        data[section][position-1][value_section] = newvalue_section
        jsonfile.seek(0)
        json.dump(data, jsonfile)
        jsonfile.truncate()

def write_monitor_info():
    monitor = screeninfo.get_monitors()[0]
    file, section = 'config.json', 'SYSTEM'
    widthscreen, heightscreen = monitor.width, monitor.height
    widthjson, heightjson = get_jsondata(file, section, 2, 'Width'), get_jsondata(file, section, 2, 'Height')
    if not widthjson == 1234 and not heightjson == 456:
        pass
    else:
        writejson('config.json', 'SYSTEM', 2, 'Width', widthscreen)
        writejson('config.json', 'SYSTEM', 2, 'Height', heightscreen)

def write_userinfo():
    file, section, position = 'config.json', 'SYSTEM', 1
    username, language = get_jsondata(file, section, position, 'Username'), get_jsondata(file, section, position, 'Language')
    if not username == 'empty' and not language == 'empty':
        pass
    else:
        username, language = Username, GetUserLanguage()
    writejson(file, section, position, 'Username', username)
    writejson(file, section, position, 'Language', language)