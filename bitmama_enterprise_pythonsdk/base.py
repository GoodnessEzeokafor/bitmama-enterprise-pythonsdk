from config import STAGING_BASE_URL,PRODUCTION_BASE_URL,SDK_ENVIRONMENTS
import httpx

# open connection 

class Base(object):
    def __init__(self, token, environment) -> None:
        if not token: raise TypeError("please enter a valid token")
        if environment not in SDK_ENVIRONMENTS: raise TypeError("please enter a valid environment")
        self._token = token  # set auth token
        self._headers = {
            'token':self._token
        } # set headers
        self._base_url = PRODUCTION_BASE_URL if environment == "production" or environment == "prod" else STAGING_BASE_URL
    
    def health(self):
        return "works"

    async def get(self, endpoint, params={}):
        '''
        function for making GET requests
        returns the data
        '''
        if not endpoint : raise TypeError("please enter a valid endpoint")
        if endpoint[0] != "/": endpoint = "/" + endpoint
        response = ''
        output_response = {}
        async with httpx.AsyncClient(headers=self._headers,base_url=self._base_url,params=params,timeout=50.0) as client:
            response = await client.get(endpoint)
        new_responses_json = response.json()
        for resp_keys,resp_values in new_responses_json.items():
            output_response[resp_keys] = resp_values
        return output_response['message']

    async def post(self,endpoint, params={}):
        '''
        function for making POST requests
        returns the data
        '''
        print(params)
        print(self._headers)
        if not endpoint : raise TypeError("please enter a valid endpoint")
        if endpoint[0] != "/": endpoint = "/" + endpoint
        response = ''
        output_response = {}
        async with httpx.AsyncClient(headers=self._headers,base_url=self._base_url) as client:
            response = await client.post(endpoint,data=params)
        new_responses_json = response.json()
        for resp_keys,resp_values in new_responses_json.items():
            output_response[resp_keys] = resp_values
        return output_response['message']


