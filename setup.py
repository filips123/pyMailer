import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='emailsend',
      version='1.0',
      description='With this module you can easy send emails.',
      url='http://github.com/fillips/pythonMail',
      author='filips',
      author_email='filip.stamcar@hotmail.com',
      license='GNU',
      packages=['mail'],
      keywords=["mail","python","send mail","module","sendmail"],
      long_description=read('README.txt'),
      platforms='any',
      classifiers=[
          "Development Status :: 4 - Beta"
          ],
      zip_safe=False)