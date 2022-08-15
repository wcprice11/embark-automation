import embark_user
import embark_session
import URLs
import element
from dotenv import load_dotenv
load_dotenv()
from os import getenv

u = embark_user.test_account
print(u.username)
print(u.get_password())
print(getenv(u.username + "_PASSWORD"))

s = embark_session.webProdSession
s.user = embark_user.test_account
s.start()

s.get(URLs.PROD_LOGIN)
s.click(element.sign_in_button)
s.fill(element.sign_in_username_field, s.user.username)
s.click(element.sign_in_next)
s.fill(element.sign_in_password_field, s.user.get_password())

