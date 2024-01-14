import requests
import smtplib
import os

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_notification(msg):
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
try:
    response = requests.get('http://13.234.48.115/')
    if response.status_code == 200:
        print('Application is running Successfully')
    else:
        print('Application Down. Fix it')
        msg = f"Application returned {response.status_code}"
        send_notification(msg)

except Exception as ex:
    print(f'Connection error encountered: {ex}')
    msg = "Application not accessible at all!!. Fix ASAP"
    send_notification(msg)