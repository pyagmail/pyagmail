# coding=utf-8
import yagmail
import keyring

# FOR GMAIL SENDER ACCOUNT NEED TO ACTIVATED THE UNSECURE APP AUTORIZATION: GO https://myaccount.google.com/security SEARCH FOR Access to less secure apps AND ENABLE IT
sender_mail = "your.unsecured@gmail.com"
sender_password = "Gmail-Password"

yagmail.register(sender_mail, password=sender_password)
