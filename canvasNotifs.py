from dotenv import load_dotenv
import pytextnow as ptn
from canvasapi import Canvas
from datetime import datetime, timedelta

USERNAME, SID, CSRF = "[USERNAME]", "[SID]" , "[CSRF]"
RECIPIENT = "<phone number>"
client = ptn.Client(USERNAME, sid_cookie=SID, csrf_cookie=CSRF)
                    
URL, TOKEN = "https://katyisd.instructure.com/", "<canvas-token>"
canvas = Canvas(URL, TOKEN)
                    
message = r"The following assignments are due in the next 48 hours:\n"
pendingAssignments = canvas.get_todo_items()
for assignment in pendingAssignments:
    name = assignment.assignment["name"]
    due = datetime.strptime(assignment.assignment["due_at"], "%Y-%m-%dT%H:%M:%SZ")
    due -= timedelta(hours=6)
    submission = assignment.assignment["submission_types"][0].replace("_", " ")
    
    if due-datetime.now() <= timedelta(hours=48):
        message += rf"- {name.strip()} at {due.strftime('%I:%M %p')} with a {submission.strip()}\n"
        
if len(message) == 57:
    message = "There are no assignments due in the next 48 hours."
    
client.send_sms(RECIPIENT, message.strip())