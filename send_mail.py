import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("Hello Adarsh")
msg['subject'] = "Integrating Mail server with Python"
msg['to'] = "your_email@gmail.com"

user = 'mail@gmail.com'
msg['from'] = user
password = 'your_password'

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user, password)
server.send_message(msg)
print(" \nEmail Sent Successfully!!")