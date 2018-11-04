import random
import time

import Models.Models as M
import coAPI.fetchData as FD
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, Personalization
import sendgrid
import os
from sendgrid.helpers.mail import Email, Content, Substitution, Mail
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib


def event_details():
    name = ["Ed-Sheeran Concert", "MAGA Rally", "Chug-the-Jug", "Cupid's Ball", "Deep Blue Destiny", "TGIF-Midnight",
            "Mexican-Fiesta", "Paradise Awaits", "Frosty Frozen Prom", "Tequila Sunrise", "Light Up the Night",
            "Zombie Prom"]
    date = ["5-Oct-2018", "9-Oct-2018", "26-Oct-2018", "8-Nov-2018", "18-Nov-2018", "4-Nov-2018", "21-Nov-2018",
            "26-Dec-2018", "8-Jan-2019"]
    price = [80, 100, 60, 150, 30, 45, 90, 200]
    location = ["Nashville, TN", "Memphis, TN", "Huntsville, AL", "New York, NY", "Salt Lake City, UT", "Denver, CO"]

    events = []
    for i in range(0, len(name)):
        events.append(
            M.Event(name[i], date[random.randint(0, len(date)-1)], location[random.randint(0,len(location)-1)],
                    price[random.randint(0,len(price)-1)]))
    return events


def cust_details():
    #customer_list = []
    custDict = FD.merchant_data() #key is name, value is email
    print(custDict)


def sendMail(scheduled_time,url,price,name):
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email("sbhandari155708@troy.edu")
    subject = "This is a test email."
    to_email = Email("spark@troy.edu")
    content = Content('text/html', 'text')
    mail = Mail(from_email, subject, to_email, content)

    dynamic_template_data = {
        'name': name,"price": price,"date":"Denver", "firstName": name, 'url':url
    }
    unixtime = time.mktime(scheduled_time.timetuple())
    mail.send_at = unixtime
    mail.personalizations[0].dynamic_template_data = dynamic_template_data
    # mail.personalizations[0].add_to(Email("jbnub12@gmail.com"))
    # mail.personalizations[0].add_substitution(Substitution('event[i].name', 'eat pray love'))
    # mail.personalizations[0].add_substitution(Substitution('event[i].price', '80'))
    # mail.personalizations[0].add_substitution(Substitution('event[i].date', '2018-Dec-14'))
    # mail.personalizations[0].add_substitution(Substitution('event[i].url', 'https://www.eventbrite.com/e/eat-pray-love-tickets-52187209348'))
    # mail.personalizations[0].add_substitution(Substitution('firstName', 'Bikram'))
    mail.template_id = "d-c9c69c9a4d164310a1c5f3c289b9d93c"
    try:
        sg.client.mail.send.post(request_body=mail.get())
    except urllib.HTTPError as e:
        e.read()
        exit()

    # sg = SendGridAPIClient()
    # mail = Mail()
    # mail.from_email = Email('sbhandari155708@troy.edu')
    # mail.template_id = 'd-c9c69c9a4d164310a1c5f3c289b9d93c'
    # p = Personalization()
    # p.add_to(Email('bhandarisaurav07@gmail.com'))
    # p.add_to(Email('blamichhane@troy.edu'))
    # p.add_to(Email('spark@troy.edu'))
    # p.dynamic_template_data = {
    #     'event[i].name': 'eat pray love',
    #     'event[i].price': '80',
    #     'event[i].date': '2018-12-14',
    #     'event[i].url': 'https://www.eventbrite.com/e/eat-pray-love-tickets-52187209348',
    #     'firstName': 'Bikram'
    # }
    # mail.add_personalization(p)
    # sg.client.mail.send.post(request_body=mail.get())



def main():
    sendMail()


if __name__ == '__main__':
    main()

