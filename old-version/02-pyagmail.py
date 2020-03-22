# coding=utf-8
import yagmail
import csv
import time
import keyring

yagmail.register('contatti.trendcolor@gmail.com', keyring.get_password("yagmail", "contatti.trendcolor@gmail.com"))
body = """Alla cortese attenzione dell'amministrazione.

L'accoglienza e la prima impressione che hanno i tuoi clienti è una fase molto importante per far percepire la tua azienda degna di fiducia, non lo pensi anche tu?

La prima impressione di un tuo potenziale cliente parte già ancor prima di un vero e proprio incontro!

Parte quando un tuo potenziale cliente visita i tuoi uffici, i tuoi locali commerciali, si immerge nel tuo ambiente di lavoro.

L’ambiente, L’arredamento e gli spazi dei tuoi locali daranno molte informazioni utili ai tuoi clienti su chi sei e come ti comporti.

L’ordine, la pulizia, l’accoglienza e l’organizzazione degli spazi in modo minuzioso, possono farti percepire dai tuoi clienti in un modo molto differente in base a come organizzerai i tuoi locali ed in base a cosa desideri far percepire loro.

Io, lo so bene, "la prima impressione è quella che conta" non lo pensi anche tu?

Mi chiamo Alessandro e dirigo un’azienda di nome Trend Color.

Noi ci occupiamo di rendere più accoglienti e più piacevoli alla vista i tuoi locali commerciali o le stanze della tua casa.

Come?

Tramite decorazioni creative di pavimenti e pareti possiamo dare un tocco di creatività, personalità e stile in più alle stanze che visiteranno i tuoi ospiti!

Che sia un bagno, una camera di albergo, una reception, un bar, un ufficio o casa tua, abbiamo una decorazione che fa al caso del tuo ambiente e dei tuoi gusti.

Possiamo perfino riuscire a creare decorazioni particolari su mobilio o qualsiasi altra superficie desideri.

Per qualsiasi tipo di atmosfera tu voglia far percepire ai tuoi ospiti, per qualsiasi tipo di arredamento i tuoi locali sono composti, noi abbiamo le decorazioni creative per pareti e pavimenti che fanno per te, per far sentire i tuoi ospiti in un ambiente ed atmosfera ben precisa.

Riuscire a far sentire un ospite parte di un determinato contesto è molto importante per dar la possibilità di essere identificati come i migliori, i più competenti, nel tuo settore.

Oltre al fatto che un ambiente ben curato e piacevole alla vista farà sentire i tuoi ospiti più coccolati ed importanti, perché parte di un ambiente esclusivo e unico!

Non lo pensi anche tu?

Per bar, ristoranti, hotel, uffici e tutti i posti in cui puoi ospitare i tuoi potenziali clienti, pianificare una consulenza gratuita con noi ti aiuterà a capire come potresti migliorare l’ambiente e renderlo più congruo a quello che vorresti comunicare con i tuoi spazi e fare sentire il tuo cliente parte di un contesto che ha una propria storia personale, che vuole comunicargli qualcosa.

Per capire meglio a quali tipologie di decorazioni mi riferisco ti consiglio di scaricare la nostra brochure tramite web, registrandoti al nostro sito tramite la pagina per <a target='_blank' href='https://trendcolor.net/go/brochure'>scaricare la brochure</a>, dopo aver scaricato la brochure dal sito, subito dopo avrai a disposizione gli estremi per contattarci e ottenere l’accesso alla lista d’attesa per il sopralluogo con preventivo gratuito.

Oppure puoi contattarmi per prenotare il sopralluogo con preventivo gratuito chiamando il numero: <a target='_blank' href='tel:+41789305001'>+41 (0)78 930 50 01</a> 

Non lasciarti scappare l’occasione di poter entrare in contatto con noi di trend color!

Siamo una realtà differente da qualsiasi altra azienda su mercato che opera nel settore delle imbiancature e decorazioni.

Noi puntiamo alla precisione nel lavoro, la puntualità della consegna e la soddisfazione dei nostri clienti!

Spero di poter rimanere in contatto.

Un cordiale saluto

Alessandro Bertrando
Director

Trend Color sagl"""
yag = yagmail.SMTP('contatti.trendcolor@gmail.com', keyring.get_password("yagmail", "contatti.trendcolor@gmail.com"))
with open('immobiliare-local-ch-locarno.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:	
        bake = time.localtime(time.time())
        if line_count == 0:
            print('Start the script')
            line_count += 1
            print(bake.tm_hour)            
        elif (bake.tm_hour <= 19 and bake.tm_hour >= 9 and line_count > 0):
            print('Sending to ' + row[line_count] + '... line processed: ')
            print(line_count)
            yag.send(
	  		    to=row[line_count],
	     	    subject="Scopri come migliorare la prima impressione per la tua azienda e per i tuoi clienti",
	    	    contents=body,
	 	    )
            line_count += 1
            time.sleep(300)
    print('Process terminated. Emails sent:' )
    print(line_count)




