from email.message import EmailMessage
import ssl
import smtplib
import json

email_sender = 'ufedofaith095@gmail.com'
email_password = 'egmvxtqxzuzkcjyg'
email_receiver =[]
with open(r"C:\Users\dvrk\Desktop\python DOV\SENDING MAILS\emailsss.json", "r") as file:
    data = json.load(file)
    for name, mail in data.items():
        receiver = mail
           
        email_receiver.append(receiver)
        print(email_receiver)
    
        
subject ='HELLO FRIEND'
body ="""How do you do my friend? """

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context ) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail (email_sender, email_receiver, em.as_string())



   

































 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
  