try:
  from setuptools import setup
except:
  from distutils.core import setup

config = {
    'description': 'exercise 48 from Learn Python the hard way',
    'author': 'Pablo Jadzinsky',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it',
    'author_email': 'pjadzinsky@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name', 'ex48'
    }

setup(**config)
