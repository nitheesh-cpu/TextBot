from urllib import response
import pytextnow as ptn
import requests

USERNAME, SID, CSRF = "[USERNAME]", "[SID]" , "[CSRF]"
RECIPIENT = "<phone number>"
client = ptn.Client(USERNAME, sid_cookie=SID, csrf_cookie=CSRF)

response = requests.get("https://api.kanye.rest/")
quote = response.json()["quote"]
quote += " -Kanye"
client.send_sms(RECIPIENT, quote)