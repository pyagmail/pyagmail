# coding=utf-8
import yagmail
import csv
import time
import keyring
import virtualconfig as cfg

print(cfg.email['email'])
print(cfg.email['passwd'])
print(cfg.email['subject'])

f = open(cfg.email['body'], 'r')
content = f.read()
f.close()

yag = yagmail.SMTP(cfg.email['email'], password=cfg.email['passwd'])

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
            print(row)
            yag.send(to=row[0], subject=cfg.email['subject'], contents=content, )
            line_count += 1
            time.sleep(cfg.email['timer'])
    print("Process terminated. Email sent: ")
    line_count -= 1
    print ( line_count )
