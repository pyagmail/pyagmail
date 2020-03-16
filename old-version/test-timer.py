
import yagmail
import csv
import time

yagmail.register('trendcolorsagl@gmail.com', 'Sciroccobianca1983')
body = """Provo ad andare a  capo

poiancora
poi ancora una volta

ciao"""
yag = yagmail.SMTP('trendcolorsagl@gmail.com', 'Sciroccobianca1983')
with open('mendrisio-chiasso-immobiliari.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:        
	bake = time.time()
        if line_count == 0:
            print('Start the script')
            line_count += 1
        elif (bake <= '19:00' and bake >= '9:00' and line_count > 0):
            print('Sending to', row[0],'...')
            yag.send(
	  		    to=row[0],
	     	    subject="Oggetto della email",
	    	    contents=body,
	 	    )
            line_count += 1
            time.sleep(300)
    print("Process terminated. created", line_count,"rows" )




