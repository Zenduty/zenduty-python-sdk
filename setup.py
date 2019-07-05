from setuptools import setup, find_packages

setup(
	name='zenduty',
	version='1.0',
	description='SDK to communicate with Zenduty API',
  author='Vishwa Krishnakumar',
	author_email='vishwa@yellowant.com',
	url='https://github.com/Zenduty/zenduty-python-sdk',
  packages=find_packages(exclude='zenduty.*'),
  install_requires=['urllib3','six'],
  scripts=['bin/client.py'])
