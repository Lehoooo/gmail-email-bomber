# Made By github.com/Lehoooo
######################################
import smtplib
import ssl
from datetime import datetime

messagessent = 0
port = 465
sslcontext = ssl.create_default_context()
######################################

print("""
________  _____ ______   ________  ___  ___               ________  ________  ________  _____ ______   _____ ______   _______   ________     
|\   ____\|\   _ \  _   \|\   __  \|\  \|\  \             |\   ____\|\   __  \|\   __  \|\   _ \  _   \|\   _ \  _   \|\  ___ \ |\   __  \    
\ \  \___|\ \  \\\__\ \  \ \  \|\  \ \  \ \  \            \ \  \___|\ \  \|\  \ \  \|\  \ \  \\\__\ \  \ \  \\\__\ \  \ \   __/|\ \  \|\  \   
 \ \  \  __\ \  \\|__| \  \ \   __  \ \  \ \  \            \ \_____  \ \   ____\ \   __  \ \  \\|__| \  \ \  \\|__| \  \ \  \_|/_\ \   _  _\  
  \ \  \|\  \ \  \    \ \  \ \  \ \  \ \  \ \  \____        \|____|\  \ \  \___|\ \  \ \  \ \  \    \ \  \ \  \    \ \  \ \  \_|\ \ \  \\  \| 
   \ \_______\ \__\    \ \__\ \__\ \__\ \__\ \_______\        ____\_\  \ \__\    \ \__\ \__\ \__\    \ \__\ \__\    \ \__\ \_______\ \__\\ _\ 
    \|_______|\|__|     \|__|\|__|\|__|\|__|\|_______|       |\_________\|__|     \|__|\|__|\|__|     \|__|\|__|     \|__|\|_______|\|__|\|__|
                                                             \|_________|                                                                     
                                                                                                                                              
                                                                                                                                              
""")

print("\n\n\nMade By github.com/Lehoooo\n\n\n")

youremail = str(input("Enter your Gmail Email: "))
yourpass = str(input("Enter your Gmail Password: "))
reciever = str(input("Enter the recievers email: "))
message = str(input("Enter what you would like to send to the reciever: "))

connection = smtplib.SMTP_SSL("smtp.gmail.com", port, context=sslcontext)
connection.login(youremail, yourpass)


while True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    connection.sendmail(youremail, reciever, message)

    print("----------------------------------------")
    print("Sent. Current Time Is: " + current_time)
    print("Emails Sent: " + str(messagessent))
    messagessent += 1
    print("----------------------------------------")

