import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'mid'
email['to'] = 'aaronseba2008@gmail.com'
email['subject'] = 'congratulations u have won a tour of the failure management headquarters'
email.set_content('god is good')
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('a35176042@gmail.com', '123456782@')
#     smtp.send_message(email)
try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('a35176042@gmail.com', '123456782@')
        smtp.send_message(email)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")
#this is to test git