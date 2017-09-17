from emailsend import sendMail

serverURL = "" #SMTP server URL
serverPort = 0 #SMTP server PORT

serverUser = "" #SMTP server username
serverPass = "" #SMTP server password

fromAddress = "" #sender email
toAddress = "" #receiver email

mSubject = "Python!" #message subject
mAttachment = [] #message attachments

mBody = "Hi!\nHow are you?\nHere is the link you wanted:\nhttps://www.python.org" #message plan text
mBodyHTML = """\
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       <b>Here is the <a href="https://www.python.org">link</a> you wanted.</b>
    </p>
  </body>
</html>
""" #message HTML text

sendmail(fromAddress, toAddress, mSubject, mBody, mBodyHTML, mAttachment, True, serverServer, serverPort, True, serverUser, serverPass)