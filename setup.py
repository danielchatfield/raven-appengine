try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='raven_appengine',
    author='Daniel Chatfield',
    author_email='chatfielddaniel@gmail.com',
    version='0.0.1',
    url='http://github.com/danielchatfield/raven-appengine',
    py_modules=['raven_appengine'],
    description='A raven transport that uses the appengine deferred library.',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python'
    ],
)