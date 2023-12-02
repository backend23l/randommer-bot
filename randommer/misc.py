import requests
from .randommer import Randommer


class Misc(Randommer):
    def get_cultures(self, api_key: str) -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key

        Returns:
            list: list of cultures
        '''
        endpoint = "Misc/Cultures"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        respons = requests.get(url,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
    
    def get_random_address(self, api_key: str, number: int, culture='en') -> list:
        '''get available misc cultures

        Args:
            api_key (str): api key
            number (str): number
            culture (str): culture

        Returns:
            list: random address
        '''
        endpoint = "Misc/Random-Address"
        url = self.get_url() + endpoint
        payload = {
            "number":number,"culture":culture
        }
        headrs = {
            "X-Api-Key":api_key
        }
        respons = requests.get(url=url,params=payload,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
