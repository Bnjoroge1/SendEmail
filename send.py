from datetime import datetime
import pyinputplus as pypi
user_name = pypi.inputStr("Enter your name please: ")   

user_email = pypi.inputEmail("Enter your email please: ").lower()

password = pypi.inputPassword("""\n Your email password is needed for authentication with GMAIL. \n
Enter your email password: """)
name_input = pypi.inputStr("Enter the name of the person you wish to send the email: ")
email_input = pypi.inputEmail("Enter his/her email as well: ").lower()

def send_msg():
        welcome_message = """ Hi {0}
        Welcome to {1}. We are so happy to have you""" .format(name_input, "instagram.com")
        return welcome_message
