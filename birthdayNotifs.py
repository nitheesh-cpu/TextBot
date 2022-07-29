from dotenv import load_dotenv
import pytextnow as ptn
from datetime import datetime, timedelta

load_dotenv()
birthdays = {
    "01-01":["Bill"],
}

USERNAME, SID, CSRF = "[USERNAME]", "[SID]" , "[CSRF]"
RECIPIENT = "<phone number>"
client = ptn.Client(USERNAME, sid_cookie=SID, csrf_cookie=CSRF)

now = datetime.now()
tomorrow = now + timedelta(hours=24)

def getBirthdays():
    message = r""
    if now.strftime("%m-%d") in birthdays.keys():
        message+=r"The following people have a birthday today:\n"
        message+= str(birthdays[now.strftime("%m-%d")])
    if tomorrow.strftime("%m-%d") in birthdays.keys():
        message+=r"\n\nThe following people have a birthday tomorrow:\n"
        message+= str(birthdays[tomorrow.strftime("%m-%d")])
    if message == "":
        nextBirthday = now
        while nextBirthday.strftime("%m-%d") not in birthdays.keys():
            nextBirthday = nextBirthday + timedelta(hours=24)
        message+=r"The next birthday is:\n"
        message+=nextBirthday.strftime("%B %d")+" : "
        message+= str(birthdays[nextBirthday.strftime("%m-%d")])
    return message

def getTomorrow():
    message = r""
    if tomorrow.strftime("%m-%d") in birthdays.keys():
        message+=r"\n\nThe following people have a birthday tomorrow:\n"
        message+= str(birthdays[tomorrow.strftime("%m-%d")])
    return message


if __name__ == "__main__":
    message = r""
    if now.strftime("%m-%d") in birthdays.keys():
        message+=r"The following people have a birthday today:\n"
        message+= str(birthdays[now.strftime("%m-%d")])
    if tomorrow.strftime("%m-%d") in birthdays.keys():
        message+=r"\n\nThe following people have a birthday tomorrow:\n"
        message+= str(birthdays[tomorrow.strftime("%m-%d")])
    if message != "":
        client.send_sms(RECIPIENT, message.strip())
    
    
