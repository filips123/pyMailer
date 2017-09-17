import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name = 'emailsend',
      version = '1.1',
      description = 'With this module you can easy send emails.',
      url = 'http://github.com/filips123/pythonMail',
      download_url = 'https://github.com/filips123/pythonMail/tarball/v1.1',
      author = 'filips',
      author_email = 'filip.stamcar@hotmail.com',
      license = 'GNU',
      packages = ['emailsend'],
      keywords = ["mail","python","send email"],
      long_description = read('README.rst'),
      platforms = 'any',
      classifiers = [
        'Programming Language :: Python :: 3',
      ],
      zip_safe = False)