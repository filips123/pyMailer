With this module you can easy send emails.

INSTALATION
===========
Run 'py setup.py install' or 'python setup.py install'

USAGE
=====
See example.py file.

from emailsend import sendmail
sendmail(fromAddress='sender_email', toAddress='receiver_email', mPassword='sender_password (optional)', mServer='mail_server', mPort='mail_port (int)', mSubject='subject', mMessage='plan_text_message (optional)', mMessageHTML='html_message (optional)',   mAttachment='attachment (optional) (list)', displaySend='login_to_server (True/False) (default=True)')

Due to a bug send attachments can not be. Instead of badges use None.
---------------------------------------------------------------------
