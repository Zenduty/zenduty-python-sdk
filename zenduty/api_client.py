from .rest import RESTClientObject
from .configuration import Configuration
class ApiClient:
    def __init__(self,access_token):
        self.configuration = Configuration(access_token)
        self.rest_client = RESTClientObject()

    def call_api(self,method,url,body={},headers={}):
        #building the header
        url ='https://www.zenduty.com'+url
        headers['Authorization']='Token '+self.configuration.access_token
        #making the request through RESTClientObject
        return self.rest_client.request(method,url,body,headers)
