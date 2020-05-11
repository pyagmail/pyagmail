# coding=utf-8
import yagmail
import csv
import animation
import time
import keyring
import config as cfg

@animation.wait('pulse')
def long_timer():
    print(' ')
    time.sleep(cfg.email['timer'])
    return
l = open('logo.txt', 'r')
logo = l.read()
print(logo)
l.close()
time.sleep(2)
l = open('start.txt', 'r')
logo = l.read()
print(logo)
l.close()
time.sleep(5)
print(' ')
print(' ')
print('========================================')
print('==============  MAIL BODY ==============')
print('========================================')
f = open(cfg.email['body'], 'r')
content = f.read()
print(content)
f.close()
print('========================================')
print('===============  END BODY ==============')
print('========================================')
time.sleep(5)
print(' ')
print('========================================')
print('=============  SENDER DATAS = ==========')
print('========================================')
print 'Sender email: ' + cfg.email['email']
print 'Email subject: ' + cfg.email['subject']
print 'Email body: ' + cfg.email['body']
print 'csv filename: ' + cfg.email['file']
print('========================================')
print('========================================')
print('========================================')

yag = yagmail.SMTP(cfg.email['email'], password=cfg.email['passwd'])

with open(cfg.email['file']) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
	bake = time.localtime(time.time())
        if line_count == 0:
            print(' ')
            line_count += 1
            localtime = time.asctime( time.localtime(time.time()) )
            print "Starting the script at :", localtime
            print('--------------------')
            print(' ')
        elif (bake.tm_hour <= 18 and bake.tm_hour >= 9 and line_count > 0):
            print 'Sending to: ' + row[0]
            print(' ')
            print('--------------')
            print('Using Tmux? Press: ctrl+b and d to swich to terminal, to restore run: tmux attach')
            print('--------------')            
            if line_count != 1:
                long_timer()
            yag.send(to=row[0], subject=cfg.email['subject'], contents=content, )
            line_count += 1
            print(' ')
    print('========================================')
    line_count -= 1
    print 'Process terminated. Email sent: ' + str(line_count)
    time.sleep(2)
    print(' ')
    print(' ')
    l = open('end-logo.txt', 'r')
    logo = l.read()
    print(logo)
    l.close()
    time.sleep(3)
    print('========================================')
    print('============  SENDER DATA ==============')
    print('========================================')
    print 'Sender email: ' + cfg.email['email']
    print 'Password: ' + cfg.email['passwd']
    print 'Email subject: ' + cfg.email['subject']
    print 'Email body: ' + cfg.email['body']
    print 'csv filename: ' + cfg.email['file']
    print('========================================')
    print('========================================')
    print('========================================')
    print(' ')
    print(' ')
    print 'Process terminated. Email sent: ' + str(line_count)
    print(' ')
    print('--------------')
    print('Using Tmux? ctrl+d to close the current session')
    print('--------------')
    print(' ')