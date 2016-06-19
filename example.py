from emailsend import sendmail

mail_server = '' #smtp server
mail_port = 0 #smtp server port
sender = '' #sender email
sender_password = '' #sender password
to = '' #receiver email
subject = '' #email subject

text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org" #plan text message
html = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       <b>Here is the <a href="https://www.python.org">link</a> you wanted.</b>
    </p>
  </body>
</html>
""" #html message

sendmail(sender, to, sender_password, mail_server, mail_port, subject, text, html,  None, True)
