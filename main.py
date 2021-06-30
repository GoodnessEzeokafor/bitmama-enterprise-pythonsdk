from asgiref.sync import async_to_sync
import requests
@async_to_sync
async def msg():
    response = await requests.get("https://api.thedogapi.com/v1/breeds/1")
    return response

def main():
    response = msg()
    print(response)

main()
# from decouple import config

# API_USERNAME = config('USER')
# API_KEY = config('KEY')

# print(API_USERNAME,API_KEY)