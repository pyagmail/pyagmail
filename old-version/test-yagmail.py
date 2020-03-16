import yagmail

yagmail.register('trendcolorsagl@gmail.com', 'Sciroccobianca1983')
receiver = "antonio.trento@yahoo.com"
body = """Provo ad andare a  capo

poiancora
poi ancora una volta

ciao"""
yag = yagmail.SMTP("trendcolorsagl@gmail.com", "Sciroccobianca1983")
yag.send(
     to=receiver,
     subject="Secondo Invio di prova da trendcolor",
     contents=body,
 )

