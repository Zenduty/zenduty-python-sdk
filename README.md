# Zenduty Python SDK

Python SDK to communicate with zenduty endpoints

## Installing

Installation can be done through pip, as follows:
```
$ pip install zenduty-api
```
or you may grab the latest source code from GitHub:
```
$ git clone https://github.com/Zenduty/zenduty-python-sdk
$ python3 setup.py install
```
## Contents
1) zenduty/api : contains the functions to communicate with zenduty API endpoints
2) zenduty/    : contains the common required files
3) bin/		   : contains sample script to run zenduty functions

## Getting started

Before you begin making use of the SDK, make sure you have your Zenduty Access Token.

You can then import the package into your python script.
```
import zenduty
```
Based on the endpoint you want to communicate with, create an object of the required class. For example, to create an incident:
```
api_obj = zenduty.IncidentsApi(zenduty.ApiClient('your-access-token'))
body = {"service":"c7fff4c5-2def-41e8-9120-c63f649a825c",
        "escalation_policy":"a70244c8-e343-4dd0-8d87-2f767115568a",
        "user":null,
        "title":"Name of trial",
        "summary":"summary of trial"}
response = api_obj.create_incident(body)
print(response.data)
print(response.status_code)
```
Refer the comments under each function for a detailed description of it's parameters.
It is important to note that each function returns a urllib3.response.HTTPResponse object.

## Running tests

There is a sample skeleton code in bin/. Add your access token to it and modify the object and function name for testing purposes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
