# pyagmail
A python script that use gmail and csv file to send email to lists

## Prerequisites
You need to allow the sender gmail account to use unsecure app via:
- https://support.google.com/cloudidentity/answer/6260879?hl=en
Or setup the script and yagmail to use OAuth2 autorization:
- https://yagmail.readthedocs.io/en/latest/setup.html#installing-from-pypi

## Usage

Works with python 2.7, not tested with python3.

The scripts require some pyton packages (pip install package-name):

- yagmail (and dependencies)
- keyring (and dependencies, if not work use keyring.alt)
- time (and dependencies)

### Start the script

Firt thing to do is edit the file config.py all entered values must be contained in quotes '' :

email = {'subject': 'Put here the email subject',
        'body': 'filename-of-the-body.txt',
        'email': 'sender.email@gmail.com',
        'passwd': 'SenderPassword',
        'timer': 100,
        'file': 'email-list.csv'}

## To remember

- Configuring keyring
- Set google account to operate with in less security apps (google account option option security)
- Set digital signature to emails in gmail
- Set autoreply message in gmail to tell users where can contact you


## Used resouces

- https://yagmail.readthedocs.io/en/latest/setup.html#installing-from-pypi

## Usefull resources:

- https://github.com/MicroPyramid/Django-CRM
- https://realpython.com/python-send-email/
- https://julien.danjou.info/sending-emails-in-python-tutorial-code-examples/
- https://github.com/kootenpv/yagmail#username-and-password

- https://www.wikihow.com/Make-a-Countdown-Program-in-Python
- https://stackoverflow.com/questions/38825824/checking-time-for-executing-if-statement
- https://www.youtube.com/watch?v=q5uM4VKywbA
- https://github.com/dbcli/pgcli/issues/914
- https://pypi.org/project/keyring/#installing-and-using-python-keyring-lib
- https://www.programiz.com/python-programming/time
- https://martin-thoma.com/configuration-files-in-python/
- https://realpython.com/python-print/

- https://serverfault.com/questions/41693/best-practices-for-preventing-you-from-looking-like-a-spammer
- https://realpython.com/python-csv/

## Gmail stats
- https://www.lifewire.com/how-to-get-certain-email-statistics-in-gmail-1171980

# To do

- create a requirement.txt file
