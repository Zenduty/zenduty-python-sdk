from setuptools import setup, find_packages

setup(
    name="zenduty-api",
    version="0.8",
    description="Python SDK wrapper for the Zenduty API",
    long_description="Python SDK wrapper for the Zenduty API",
    long_description_content_type="text/x-rst",
    author="Vishwa Krishnakumar",
    author_email="vishwa@yellowant.com",
    packages=find_packages(),
    install_requires=[
        "requests==2.32.3",
        "urllib3==2.2.2",
        "six==1.9.0",
        "charset-normalizer==3.3.2",
        "idna==3.7",
        "certifi==2024.7.4"
    ],
)