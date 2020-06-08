import maya
import pyinputplus as pypi

user_name = pypi.inputStr("Enter your name please: ")   

user_email = pypi.inputEmail("Enter your email please: ").lower()

password = pypi.inputPassword("""\n Your email password is needed for authentication with GMAIL. \n
Enter your email password: """)
name_input = pypi.inputStr("Enter the name of the person you wish to send the email: ")
email_input = pypi.inputEmail("Enter his/her email as well: ").lower()
subject = pypi.inputStr("What is the Title of your email? \n")
#date_sent = pypi.inputDatetime(" WHen do you want to send teh email? ")
def send_msg():
        welcome_message = pypi.inputStr('''Enter your message: \n
        ''')
        print(maya.now())
        return welcome_message
