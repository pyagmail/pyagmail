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

- Create a email-list.csv file

In this file, will be read the email list to which to send the emails, for each line a different email, the script will scan this file, line by line, and send the emails to each address read. the first line of the file is not read by the script (you can name as you wish, remember to put the same name into config.py file and put in the same path of the project and use .csv extension).

- Create a filename-of-the-body.txt file:

This file contain the body of the email you need to use the right encode, to be read correctly by the python interpreter, in this file, https://github.com/pyagmail/pyagmail/blob/master/string-encoding-python.md there are some reference links and documentation to understand the problem (you can name as you wish, remember to put the same name into config.py file and put in the same path of the project and use .txt extension).

- Edit the file config.py all entered values must be contained in quotes '' (apart timer field, it don't need '') :

``` python
email = {'subject': 'Put here the email subject',
        'body': 'filename-of-the-body.txt',
        'email': 'sender.email@gmail.com',
        'passwd': 'SenderPassword',
        'timer': 100,
        'file': 'email-list.csv'}
```

The timer field is the time expressed in seconds between sending an email and the other, the value 100 is about 2 minutes.

- Run for 1 time the keyring-registration.py file set the same password of your sender email password:

``` bash
python keyring-registration.py
```
This will store into linux keyring system the yagmail autorization to use and run the machine.

- Run the pyagmail.py script to start sending mail:

``` bash
python pyagmail.py
```

launching the script you will need to leave the terminal window open to complete it, otherwise it will stop.

Since, depending on the length of the list, the execution of the script may take days, to overcome the problem of keeping the terminal open, if you use linux, you can take advantage of tmux to launch the script in the background:
- https://github.com/tmux/tmux/wiki

Some solution to run in background with windows:
- https://superuser.com/questions/408874/tmux-screen-alternative-for-powershell

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
