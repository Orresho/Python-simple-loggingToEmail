import json
import os
import sendgrid
from sendgrid.helpers.mail import *
import base64
import logging

# Create logger
log = logging.getLogger('Exmaple')
log.setLevel(logging.DEBUG)

def configureLog():

    # basic configuration with formatting
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='spam.log', filemode='w')

    someMessagesExample()
    
# Mock messages
def someMessagesExample():
    log.info('This is pretty cool.')
    log.info('May the force be with you, k bye')
    

def encodeFromFileAndSendToEmail():
    file_path = "spam.log"
    encoded = ''
    with open(file_path, 'rb') as f:
        data = f.read()
        print(data)
        encoded = base64.b64encode(data).decode()
        f.close()

    # Execute the email sending process
    sendEmail(encoded)


def sendEmail(encoded):

    # Config/Setup
    sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('my_key'))
    from_email = Email("example@example.com")
    to_email = Email("example@example.com")
    subject = "Pitchler Report"
    content = Content("text/html", 'This is not a virus, i promise, click the file and good things will happen\n\n / Microsoft Pro Technician Engineer Ishwar Sirasikar')

    # Create file attachment
    attachment = Attachment()
    attachment.type = "text/plain"
    attachment.content = encoded
    attachment.filename = "W32/Conficker.txt"
    attachment.disposition = "attachment"
    attachment.content_id = "Balance Sheet"

    mail = Mail(from_email, subject, to_email, content)
    mail.add_attachment(attachment)

    response = sg.client.mail.send.post(request_body=mail.get())

    print(response.status_code)
    print(response.body)
    print(response.headers)



# Main application method
def main():
    configureLog()
    encodeFromFileAndSendToEmail()


# Run
main()
