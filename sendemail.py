import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from send import *
import pyinputplus as pypi

#Main function that sends the mail
def send_mail(text = send_msg(), subject = subject, 
    from_email = user_email , to_email = [email_input],
    html = None):
    import maya
    while True:
        assert isinstance(to_email, list)                            #Check if it's a string otherwie, return assertion error
        msg = MIMEMultipart("alternative")
        msg["From"] = from_email
        msg["To"] = "," .join(to_email)
        msg["Subject"] = subject
        text_part = MIMEText(text, "plain")
        msg.attach(text_part)
        if html != None:
            html_part = MIMEText("<h1> This is my first Email!</h1>")
            msg.attach(html_part)
            
        msg_str = msg.as_string()
        
        #Login to the STMP Servers

        with smtplib.SMTP(host = "smtp.gmail.com", port = 587) as server:
            server.ehlo()
            server.starttls()
            server.login(user_email, password)
            server.sendmail(from_email, to_email, msg_str)
            break
send_mail()
    
    
    
    
    
        
