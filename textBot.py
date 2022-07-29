import pytextnow as pytn
import tinytuya
import json
import requests
import birthdayNotifs
import datetime
from bs4 import BeautifulSoup
import schedule

USERNAME, SID, CSRF = "[USERNAME]", "[SID]" , "[CSRF]"
client = pytn.Client(USERNAME, sid_cookie=SID, csrf_cookie=CSRF)


schedules = {
    "" : "https://imgur.com/a/7KQ7nHw",
    "exam": "https://imgur.com/a/SmySJle",
    "pep": "https://imgur.com/a/PvJzwIV",
    "rally": "https://imgur.com/a/PvJzwIV",
    "peprally": "https://imgur.com/a/PvJzwIV"
}

f = open('/home/pi/snapshot.json')
devices = json.load(f)
def search (name):
    for keyval in devices['devices']:
        if name.lower() == keyval['name'].lower():
            x = tinytuya.OutletDevice(keyval['id'],keyval['ip'],keyval['key'])
            x.set_version(float(keyval['ver']))
            # print("Version: " + x.version)
            return x

print('Started!')

@client.on("message")
def handler(msg):
    print(msg)
    if msg.type == pytn.MESSAGE_TYPE:
        if msg.content[0] != '/':
            print('Message ignored')
        if msg.content == "/ping":
            msg.send_sms("pong!")
        if (str(msg.number) == '<phone number>') :
            if "/off" in msg.content:
                x = str(msg.content).replace('/off ','')
                try:
                    device = search(x)
                    data = device.status()
                    print('Device status: %r' % data)
                    device.turn_off()
                    msg.send_sms("Turning off " + str.title(x) + "...")
                except AttributeError:
                    msg.send_sms("Could not find the device \'" + x + "\'")
            elif "/on" in msg.content:
                x = str(msg.content).replace('/on ','')
                try:
                    device = search(x)
                    data = device.status()
                    print('Device status: %r' % data)
                    device.turn_on()
                    msg.send_sms("Turning on " + str.title(x) + "...")
                except AttributeError:
                    msg.send_sms("Could not find the device \'" + x + "\'")
        if "/quote" in msg.content:
            response = requests.get("https://api.kanye.rest/")
            quote = response.json()["quote"]
            quote += " -Kanye"
            msg.send_sms(quote)
        if "/assignments" in msg.content and (str(msg.number) == '<phone number>'):
            exec(open('/home/pi/canvasNotifs.py').read())
        if "/birthdays" in msg.content:
            msg.send_sms(birthdayNotifs.getBirthdays())
        if "/schedule" in msg.content:
            x = str(msg.content).replace('/schedule','')
            x = str(x).replace(' ','')
            print('\'' + x + '\'')
            if x in schedules.keys() :
                msg.send_sms(schedules[x])
        if "/reload" in msg.content:
            exit()
        if "/meme" in msg.content:
            response = requests.get("https://meme-api.herokuapp.com/gimme")
            memeLink = response.json()["url"]
            msg.send_sms(memeLink)
        if "/fact" in msg.content:
            x = msg.content.replace('/fact ','')
            link = "https://some-random-api.ml/animal/" + x
            response = requests.get(link)
            try:
                fact = response.json()["fact"]
            except json.JSONDecodeError:
                fact = "Could not find that animal"
            print(fact)
            msg.send_sms(fact)
        if "/help" in msg.content:
            text = r"Commands: \n/quote\n/birthdays\n/schedule <type>\n/reload\n/meme\n/fact <animal>\n/weather\n/joke\n/news\n/apod\n"
            msg.send_sms(text.strip())
        if "/weather" in msg.content:
            weather = requests.get("http://api.openweathermap.org/data/2.5/weather?q=<city>,<country>&APPID=<api-id>&units=imperial")
            msg.send_sms(str.title(weather.json()["weather"][0]["description"]) + " - " + str(weather.json()["main"]["temp"]) + "°F")
        if "/apod" in msg.content:
            apod = requests.get("https://api.nasa.gov/planetary/apod?api_key=<key>")
            msg.send_sms(str.title(apod.json()["title"]) + ": " + str(apod.json()["explanation"]))
            msg.send_sms(apod.json()["hdurl"])
        if "/news" in msg.content:
            news = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=<key>")
            msg.send_sms(str.title(news.json()["articles"][0]["title"]) + ": " + str(news.json()["articles"][0]["description"]))
            msg.send_sms(news.json()["articles"][0]["url"])
        if "/joke" in msg.content:
            joke = requests.get("https://icanhazdadjoke.com/", headers={"Accept":"application/json"})
            msg.send_sms(joke.json()["joke"])
        if "/checkschedule" in msg.content:
            msg.send_sms(schedule.getSchedule())
