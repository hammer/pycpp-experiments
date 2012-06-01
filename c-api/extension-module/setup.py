from distutils.core import setup, Extension

spam = Extension('spam',
                 sources = ['spammodule.c'])

setup (name = 'spam',
       version = '1.0',
       description = 'spam',
       ext_modules = [spam])
