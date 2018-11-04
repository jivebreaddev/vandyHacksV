# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient('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')
from_email = Email("sbhandari155708@troy.edu")
to_email = Email("bhandarisaurav07@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
