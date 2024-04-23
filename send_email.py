import smtplib, ssl, time

host = "smtp.gmail.com"
port = 465

username = "perzak102@gmail.com"
password = "fzgqivtksrnlspuk"

receiver = "perzak102@wp.pl"
context = ssl.create_default_context()

message = """\
Subject: Hi!
How are you?
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)