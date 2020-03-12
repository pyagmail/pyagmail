import yagmail
import csv
import time
import keyring
import config as cfg

yagmail.register(cfg.email['email'], cfg.email['passwd']) #need to be set the keyring in the password field: keyring.get_password("system", "user")
yag = yagmail.SMTP(cfg.email['email'], cfg.email['passwd']) #need to be set the keyring in the password field: keyring.get_password("system", "user")
with open(cfg.email['file']) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:        
	bake = time.localtime(time.time())
        if line_count == 0:
            print('Start the script')
            line_count += 1
        elif (bake.tm_hour <= 19 and bake.tm_hour >= 9 and line_count > 0):
            print('Sending to ' + cfg.email['email'] + '...')
            yag.send(
	  	    to=row[0],
	     	    subject=cfg.email['subject'],
	    	    contents=cfg.email['body'],
	 	    )
            line_count += 1
            time.sleep(cfg.email['time'])
    print("Process terminated. created " + line_count  + " rows" )
