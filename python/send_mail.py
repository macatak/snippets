import smtplib

fromaddr = "spam@eggs.com"
toaddr = "eggs@spam.com"
subject = "Premium Spam"
msg = "test\ntest2"
message = 'Subject: {} \n\n{}'.format(subject,msg)

server=smtplib.SMTP('localhost')
server.set_debuglevel(1)
server.sendmail(fromaddr, toaddr, message)
server.quit()
