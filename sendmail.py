from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

smtp_host = "smtprelay.moh.gr"
port = 25  # For SSL
sender_email = "Optimax - Berth Scheduling Platform <dockassist@moh.gr>"


def sendmail(recipients, message):
    cc = ''
    bcc = ''
    msg = MIMEMultipart('related')
    msg['Subject'] = message
    msg['From'] = sender_email
    msg['To'] = ','.join(recipients)

    msg.preamble = 'This is a multi-part message in MIME format.'

    msgText = MIMEText('''<html> \
            <body><font face = "Verdana" size = "12" /><div style="background: orange; color:#363640; font-face:Verdana;" \
            <p>--- This is an automated email - Do not reply ---<p> \
            </html> '''.format(**locals()), 'html')

    msg.attach(msgText)

    smtp = smtplib.SMTP()
    smtp.connect(smtp_host)
    smtp.ehlo()
    smtp.sendmail(sender_email, recipients, msg.as_string())
    smtp.quit()


#recipients = ['andreas.sakellariou@gmail.com','mary.levandi@gmail.com']
#sendmail(recipients, 'TEST')