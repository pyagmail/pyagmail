# coding=utf-8
import yagmail
import csv
import time
import keyring
import config as cfg

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
        elif (bake.tm_hour <= 18 and bake.tm_hour >= 9 and line_count > 0):
            print('Sending to: ')
            print(row)
            if line_count != 1:
                time.sleep(cfg.email['timer'])
            yag.send(to=row[0], subject=cfg.email['subject'], contents=content, )
            line_count += 1
    print("Process terminated. Email sent: ")
    line_count -= 1
    print ( line_count )
