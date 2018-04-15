import smtplib

def emailNotification(toAddress, courseString):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    #Next, log in to the server
    server.starttls()
    server.login("utilitycds@gmail.com", "%camUni1%")

    #Send the mail
    msg = "Hello there is a spot open in " + courseString
    server.sendmail("utilitycds@gmail.com", toAddress, msg)
    server.quit()