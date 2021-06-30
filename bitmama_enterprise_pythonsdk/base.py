from config import STAGING_BASE_URL,PRODUCTION_BASE_URL,SDK_ENVIRONMENTS
import httpx
import trio
import os

# open connection 

class Base(object):
    def __init__(self, token, environment) -> None:
        # data = dict(kwargs.get("data"))
        # print(data)
        # token = data['token']
        # environment = data["environment"]
        if not token: raise TypeError("please enter a valid token")
        if environment not in SDK_ENVIRONMENTS: raise TypeError("please enter a valid environment")
        self._token = token  # set auth token
        self._headers = {
            'token':self._token
        } # set headers
        self._base_url = PRODUCTION_BASE_URL if environment == "production" or environment == "prod" else STAGING_BASE_URL
    
    def health(self):
        return "works"

    async def get(self, endpoint, **kwargs):
        '''
        function for making GET requests
        returns the data
        '''
        if not endpoint : raise TypeError("please enter a valid endpoint")
        if endpoint[0] != "/": endpoint = "/" + endpoint
        response = ''
        output_response = {}
        async with httpx.AsyncClient(headers=self._headers,base_url=self._base_url,params=kwargs) as client:
            response = await client.get(endpoint)
        new_responses_json = response.json()
        for resp_keys,resp_values in new_responses_json.items():
            output_response[resp_keys] = resp_values
        return output_response

    async def post(self,endpoint, params):
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
        return output_response

    def get_base_url(self):
        return self._base_url

# if __name__ == "__main__":
#     api = Base('3ee3701e057b26c6b55d0bee2', "dev")
#     print(api.health())
#     print(api.get_base_url())
#     print(api.get_url())    
#     run_get = trio.run(api.get)
#     # run_post = trio.run(api.post)
#     # # trio.run(print(api.post))
#     print(run_get['code'])
#     # resp_dict={}
#     # # resp_dict -
#     # for resp_keys,resp_values in run_get.items():
#     #     # print(resp_keys, ":", resp_values)
#     #     resp_dict[resp_keys] = resp_values
#     # print("----------new dictionary-------------")
#     # print("new oh",resp_dict['message'])
#     # print("----------new dictionary-------------")