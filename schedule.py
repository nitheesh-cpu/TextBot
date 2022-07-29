import requests
from bs4 import BeautifulSoup
import pytextnow as pytn

login_data = {
    '__RequestVerificationToken': '',
    'SCKTY00328510CustomEnabled': True,
    'SCKTY00436568CustomEnabled': True,
    'Database': 10,
    'VerificationOption': 'UsernamePassword',
    'LogOnDetails.UserName': '',
    'tempUN': '',
    'tempPW': '',
    'LogOnDetails.Password': ''
}

USERNAME, SID, CSRF = "[USERNAME]", "[SID]" , "[CSRF]"
client = pytn.Client(USERNAME, sid_cookie=SID, csrf_cookie=CSRF)

def main():
    login_url = "https://homeaccess.katyisd.org/HomeAccess/Account/LogOn"
    assignmentsdata = 'https://homeaccess.katyisd.org/HomeAccess/Content/Student/Assignments.aspx'
    reportcarddata = 'https://homeaccess.katyisd.org/HomeAccess/Content/Student/ReportCards.aspx'

    classes = []
    averages = []

    reportcardheader = ['Course', 'Description', 'Period', 'Teacher', '1st', '2nd', '3rd', 'Exam1', 'Sem1', '4th', '5th', '6th', 'Exam2', 'Sem2']
    reportcard = []

    sendUpdate()

def getSchedule():
    with requests.Session() as session:
        login_url = "https://homeaccess.katyisd.org/HomeAccess/Account/LogOn"
        r = session.get(login_url)
        soup = BeautifulSoup(r.content, 'html.parser')
        login_data['__RequestVerificationToken'] = soup.find('input', attrs={'name': '__RequestVerificationToken'})['value']
        post = session.post(login_url, data=login_data)
        schedule = session.get('https://homeaccess.katyisd.org/HomeAccess/Content/Student/DailySchedule.aspx')
        content = BeautifulSoup(schedule.text, 'html.parser')
        with open('schedule.html', 'w') as f:
            f.write(str(content))
        if 'Demographic' in content.text:
            return 'Schedule is not up!'
        else:
            return 'Schedule is up!'

def sendUpdate():
    client.send_sms("<phone number>", getSchedule())



if __name__ == '__main__':
    main()
