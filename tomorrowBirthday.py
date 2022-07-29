import birthdayNotifs as notifs
import pytextnow as ptn

USERNAME, SID, CSRF = "[USERNAME]", "[SID]" , "[CSRF]"
RECIPIENT = "<phone number>"
client = ptn.Client(USERNAME, sid_cookie=SID, csrf_cookie=CSRF)

if __name__ == "__main__":
    message = r""
    message += notifs.getTomorrow()
    if message != "":
        client.send_sms(RECIPIENT, message.strip())