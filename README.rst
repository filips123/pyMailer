With this module you can easy send emails.

INSTALATION
===========
Run 'py setup.py install' or 'python setup.py install'

USAGE
=====
See example.py file.

.. code:: python

  from emailsend import sendMail
  sendMail(fromAddress = "sender email", toAddress = "receiver email", mSubject = "message subject", mBody = "message body", mBodyHTML = "message subject HTML", mAttachment = ["message" , "attachments", "-", "path", "to", "file", "(optional)"], serverLogin = "login to server (True/False)", serverServer = "server URL", serverPort = "server port (int)", serverTSL = "TSL (True/False), serverUser = "server userame", serverPass = "server password")