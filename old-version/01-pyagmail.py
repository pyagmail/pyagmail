import yagmail
import csv
import time

yagmail.register('trendcolorsagl@gmail.com', 'Sciroccobianca1983')	
receiver = "antonio.trento@yahoo.com"
body = """Provo ad andare a  capo

poiancora
poi ancora una volta

ciao"""
yag = yagmail.SMTP("trendcolorsagl@gmail.com", "Sciroccobianca1983")
with open("mendrisio-chiasso-immobiliari.csv") as file:
	reader = csv.reader(file)
	next(reader)  # Skip header row
for emails in reader:
	# Timer of 5 min and if statement that make the script works only on work hours
	time.sleep(1)
	bake = time()
	if (bake <= '19:00' and bake >= '9:00'):
	    # Send email here
		print("Sending email to {emails}")


