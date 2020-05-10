# coding=utf-8
import yagmail
import csv
import time
import keyring
import virtualconfig as cfg

print('========================================')
print('=================  TESTO ================')
print('========================================')
f = open(cfg.email['body'], 'r')
content = f.read()
print(content)
f.close()
print('========================================')
print('===============  FINE TESTO  ===============')
print('========================================')
print(' ')
print('========================================')
print('================  DATI DI INVIO  =============')
print('========================================')
print('Sender email:')
print(cfg.email['email'])
print('Password:')
print(cfg.email['passwd'])
print('Email subject')
print(cfg.email['subject'])
print('Email body')
print(cfg.email['body'])
print('csv filename:')
print(cfg.email['file'])
print('========================================')
print('========================================')
print('========================================')

with open(cfg.email['file']) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
	bake = time.localtime(time.time())
        if line_count == 0:
            print('Start the script')
            line_count += 1
            print('At time:')
            print(bake.tm_hour)
        elif (line_count > 0):
            print('Sending to: ')
            print(row[0])
            if line_count != 1:
                time.sleep(cfg.email['timer'])
            line_count += 1
    print('========================================')
    print("Process terminated. Email sent: ")
    line_count -= 1
    print ( line_count )
