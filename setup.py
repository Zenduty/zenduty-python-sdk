from setuptools import setup, find_packages

setup(
	name='zenduty-api',
	version='0.1',
	description='Python SDK wrapper for the Zenduty API',
	long_description='Python SDK wrapper for the Zenduty API',
	long_description_content_type="text/x-rst",
  author='Vishwa Krishnakumar',
	author_email='vishwa@yellowant.com',
  packages=find_packages(),
  install_requires=['urllib3','six==1.9.0'],
  scripts=['bin/client.py'])
