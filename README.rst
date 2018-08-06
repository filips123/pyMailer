With this module you can easy send emails.

INSTALATION
===========

**Warning:**

Due the error in deployment, the module was deleted.

Please download module directly from `PyPI <https://pypi.org/project/emailsend/>`_ using PIP.
Alternatively, you can install module `from .tar.gz file from PyPI <https://files.pythonhosted.org/packages/5c/a5/b653104cf78adb90c8a41b43f43eaea85134bc4d2f462d645c0ece81810f/emailsend-1.1.tar.gz>`_.

Run 'py setup.py install' or 'python setup.py install'

USAGE
=====
See example.py file.

.. code:: python

  from emailsend import sendMail
  sendMail(fromAddress = "sender email", toAddress = "receiver email", mSubject = "message subject", mBody = "message body", mBodyHTML = "message subject HTML", mAttachment = ["message" , "attachments", "-", "path", "to", "file", "(optional)"], serverLogin = "login to server (True/False)", serverServer = "server URL", serverPort = "server port (int)", serverTSL = "TSL (True/False), serverUser = "server userame", serverPass = "server password")
