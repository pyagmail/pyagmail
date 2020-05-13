# coding=utf-8
import yagmail
import csv
import animation
import time
import keyring
import logging
import config as cfg

@animation.wait('pulse')
def long_timer():
    print(' ')
    time.sleep(cfg.email['timer'])
    return
@animation.wait('pulse')  
def night_timer(sec):
  time.sleep(sec)
  return
LOG_FILE_ONE = "sent.log"
LOG_FILE_TWO = "pyagmail.log"
def main():
  setup_logger('log_one', LOG_FILE_ONE)
  setup_logger('log_two', LOG_FILE_TWO)

def setup_logger(logger_name, log_file, level=logging.INFO):
  log_setup = logging.getLogger(logger_name)
  formatter = logging.Formatter('%(levelname)s: %(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
  fileHandler = logging.FileHandler(log_file, mode='a')
  fileHandler.setFormatter(formatter)
  streamHandler = logging.StreamHandler()
  streamHandler.setFormatter(formatter)
  log_setup.setLevel(level)
  log_setup.addHandler(fileHandler)
  log_setup.addHandler(streamHandler)

def logger(msg, level, logfile):
  if logfile == 'one'   : log = logging.getLogger('log_one')
  if logfile == 'two'   : log = logging.getLogger('log_two') 
  if level == 'info'    : log.info(msg) 
  if level == 'warning' : log.warning(msg)
  if level == 'error'   : log.error(msg)

if __name__ == "__main__":
  main()
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
filename = raw_input("Enter csv file name of the email list or leave empty and press enter for use the default filename from config.py: ")
if filename:
  cfg.email['file'] = filename
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
try:
  yag = yagmail.SMTP(cfg.email['email'], password=cfg.email['passwd'])
  print ('SMTP connection established!')
  # logging.info('SMTP connection established! With csv file ' + cfg.email['file'])
  message = 'Starting script SMTP connection established! WITH CSV FILE ' + cfg.email['file']
  logger(message, 'info', 'one')
  logger(message, 'warning', 'two')
except:
  print ('SMTP connection ERROR!')
  # logging.warning('SMTP connection REFUSED! With csv file ' + cfg.email['file'])
  message = 'SMTP connection REFUSED! With csv file ' + cfg.email['file']
  logger(message, 'warning', 'two')

with open(cfg.email['file']) as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    bake = time.localtime(time.time())
    if (bake.tm_hour > 18 or bake.tm_hour < 9 and line_count > 0):
      if (bake.tm_hour >= 0 and bake.tm_hour <= 8):
        ora = bake.tm_hour * 3600
        sec = 32400 - ora
      else:
        ora = 24 - bake.tm_hour
        ora = ora * 3600
        sec = ora + 32400
      print "It's :", localtime
      print "Waiting for 9:00 o clock..."
      night_timer(sec)
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
      try:
        yag.send(to=row[0], subject=cfg.email['subject'], contents=content, )
        count = line_count
        line_count += 1
        print(' ')
        print(row[0] + ' Email sent! Go on!')
        message='Email sent! ' + row[0] + ' in csv file ' + cfg.email['file'] + ' in line: ' + str(count)
        logger(message, 'info', 'one')
        print(' ')
        # logging.info('Email sent! ' + row[0] + ' in csv file ' + cfg.email['file'] + ' in line: ' + str(count))
        print(' ')
      except:
        print(' ')
        print(row[0] + ' ERROR the email is not valid! Go on!')
        print(' ')
        count = line_count
        # logging.warning('ERROR the email is not valid! ' + row[0] + ' in csv file ' + cfg.email['file'] + ' in line: ' + str(count))
        message='ERROR the email is not valid! ' + row[0] + ' in csv file ' + cfg.email['file'] + ' in line: ' + str(count)
        logger(message, 'warning', 'two')
        print(' ')
print('========================================')
line_count -= 1
print 'Process terminated. Email sent: ' + str(line_count)
# logging.info('PROCESS TERMINATED! Number of mail sent: ' + str(count) + ' in csv file ' + cfg.email['file'])
message= 'PROCESS TERMINATED! Number of mail sent: ' + str(count) + ' in csv file ' + cfg.email['file']
logger(message, 'info', 'one')
logger(message, 'warning', 'two')
time.sleep(2)
print(' ')
print(' ')
l = open('end-logo.txt', 'r')
logo = l.read()
print(logo)
l.close()
time.sleep(3)
print('========================================')
print('============  SENDER DATA ===========')
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
print(' ')
oggetto_finale = "Report Pyagmail file: " + cfg.email['file']
if line_count != 0:
  mail_finale = "Email sent with Pyagmail " + str(line_count) + " mail dal file " + cfg.email['file'] + ". Controlla i file di log allegati alla mail per capire quante operazioni di invio sono andate a buon fine."
else:
  mail_finale = "ERROR on pyagmail mail sent: " + str(line_count) + " mail from file: " + cfg.email['file'] + ". Check file.csv with lists is correct try to run again the script"
print('--------------')
print oggetto_finale
print(' ')
print mail_finale
print('--------------')
try:
  yag.send(to=cfg.email['log_email'], subject=oggetto_finale, contents=mail_finale, attachments=['pyagmail.log','sent.log'])
except:
  print('It was impossible to send the log email to the receiver check if the email is correct!')
print (' ')
print('--------------')
print('Using Tmux? ctrl+d to close the current session')
print('--------------')
print(' ')
