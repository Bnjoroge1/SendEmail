import imaplib
import email

host  = "imap.gmail.com"
user_name = "williamsriunge@gmail.com"
password = "11235150"

mail = imaplib.IMAP4_SSL(host)
mail.login(user_name, password)
mail.select("inbox")

_,search_data = mail.search(None, "UNSEEN")
print(search_data)




