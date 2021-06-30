from config import STAGING_BASE_URL,PRODUCTION_BASE_URL,SDK_ENVIRONMENTS
import httpx
import trio
import os

# open connection 

class Api:
    def __init__(self, token, environment,url='/rate') -> None:
        if not token: raise TypeError("please enter a valid token")
        if environment not in SDK_ENVIRONMENTS: raise TypeError("please enter a valid environment")
        if not url : raise TypeError("please enter a valid url")
        if url[0] != "/": url = "/" + url
        self._token = token  # set auth token
        self._headers = {
            'token':self._token,
            'Content-Type':'application/json'
        } # set headers
        self._url = url # set url
        self._base_url = PRODUCTION_BASE_URL if environment == "production" or environment == "prod" else STAGING_BASE_URL
    
    def health(self):
        return "works"

    async def get(self):
        '''
        function for making GET requests
        returns the data
        '''
        response = ''
        output_response = {}
        async with httpx.AsyncClient(headers=self._headers,base_url=self._base_url) as client:
            response = await client.get(self._url)
        new_responses_json = response.json()
        for resp_keys,resp_values in new_responses_json.items():
            output_response[resp_keys] = resp_values
        return output_response

    async def post(self):
        '''
        function for making POST requests
        returns the data
        '''
        response = ''
        output_response = {}
        async with httpx.AsyncClient(headers=self._headers,base_url=self._base_url) as client:
            response = await client.get(self._url)
        new_responses_json = response.json()
        for resp_keys,resp_values in new_responses_json.items():
            output_response[resp_keys] = resp_values
        return output_response

    def get_base_url(self):
        return self._base_url
    def get_url(self):
        return self._url

if __name__ == "__main__":
    api = Api('3ee3701e057b26c6b55d0bee2', "dev", "webhook")
    print(api.health())
    print(api.get_base_url())
    print(api.get_url())    
    run_get = trio.run(api.get)
    # run_post = trio.run(api.post)
    # # trio.run(print(api.post))
    print(run_get['code'])
    # resp_dict={}
    # # resp_dict -
    # for resp_keys,resp_values in run_get.items():
    #     # print(resp_keys, ":", resp_values)
    #     resp_dict[resp_keys] = resp_values
    # print("----------new dictionary-------------")
    # print("new oh",resp_dict['message'])
    # print("----------new dictionary-------------")