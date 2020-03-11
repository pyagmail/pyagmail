import yagmail
import csv
import time
import config as cfg

yagmail.register(cfg.email['email'], cfg.email['passwd'])
yag = yagmail.SMTP(cfg.email['email'], cfg.email['passwd'])
with open(cfg.email['file']) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:        
	bake = time.time()
        if line_count == 0:
            print('Start the script')
            line_count += 1
        elif (bake <= '19:00' and bake >= '9:00' and line_count > 0):
            print('Sending to', cfg.email['email'],'...')
            yag.send(
	  	    to=cfg.email['email'],
	     	    subject=cfg.email['subject'],
	    	    contents=cfg.email['body'],
	 	    )
            line_count += 1
            time.sleep(300)
    print("Process terminated. created", line_count,"rows" )
