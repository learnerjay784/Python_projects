# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 23:44:02 2022

@author: Admin
"""


import time
import hashlib
from urllib.request import urlopen, Request
import smtplib
import ssl
from email.message import EmailMessage

# Checking for the change in website
url = Request('https://www.aajtak.in/', headers={'User-Agent': 'Mozilla/5.0'})
response = urlopen(url).read()
currentHash = hashlib.sha224(response).hexdigest()
print("running")
PrevVersion = ""
time.sleep(10)
while True:
    try:
        time.sleep(30)
        response = urlopen(url).read()
        newHash = hashlib.sha224(response).hexdigest()
        if newHash == currentHash:
            continue
        else:
            print("something changed")
            
            #Sending email for informing about the change in website
            response = urlopen(url).read()
            currentHash = hashlib.sha224(response).hexdigest()
            time.sleep(30)
            # Sending Email Notification
            port = 465  # For SSL
            smtp_server = "smtp.gmail.com"
            sender_email = "barodejay468@gmail.com"  # Enter your address
            receiver_email = "niboso3705@pro5g.com"  # Enter receiver address
            password = '************23'   #Hidden for safety purpose
            subject = 'Website Change Notification'
            message = """
            Subject: Hi there!
            Changes have been applied to Website!
            """
            em = EmailMessage()
            em['From'] = 'barodejay468@gmail.com'
            em['To'] = 'niboso3705@pro5g.com'
            em['Subject'] = subject
            em.set_content(message)
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login('barodejay468@gmail.com', '************23')
                server.sendmail('barodejay468@gmail.com','niboso3705@pro5g.com' , em.as_string())
            continue
    except Exception as e:
        print(e)