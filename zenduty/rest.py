import urllib3
import json

from .exceptions import ApiException, ApiValueError

class RESTClientObject(object):
    def __init__(self):
        self.pool_manager = urllib3.PoolManager()

    def request(self,method,url,body,headers):
        #verifying the method
        method = method.upper()
        assert method in ['GET', 'DELETE', 'POST', 'PATCH']
        #verifying Content-type
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'
        #Making the request
        try:
            if method=='GET':
                return self.pool_manager.request(method,url,headers=headers)
            else:
                request_body = None
                if body is not None:
                    request_body = json.dumps(body)
                return self.pool_manager.request(method,url,body=request_body,headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)
