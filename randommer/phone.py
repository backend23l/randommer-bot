import requests
from .randommer import Randommer


class Phone(Randommer):
    def generate(self, api_key: str, CountryCode: str, Quantity: int) -> list:
        '''get bulk telephone numbers for a country

        Args:
            api_key (str): api key
            CountryCode (str): CountryCode ex: 'uz'
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint = "Phone/Generate"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        params = {
            "CountryCode":CountryCode,"Quantity":Quantity
        }
        respons = requests.get(url=url,params=params,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
        
    def get_IMEI(self, api_key: str, Quantity: int) -> list:
        '''get bulk imei

        Args:
            api_key (str): api key
            Quantity (str): Quantity

        Returns:
            list: list of phone numbers
        '''
        endpoint = "Phone/IMEI"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        params = {
            "Quantity":Quantity
        }
        respons = requests.get(url=url,params=params,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
    
    def is_valid(self, api_key: str, telephone: str, CountryCode: str) -> bool:
        '''get bulk imei

        Args:
            api_key (str): api key
            telephone (str): phone number
            CountryCode (str): CountryCode ex: 'uz'

        Returns:
            bool: is valid
        '''
        endpoint = "Phone/Validate"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        params = {
            "telephone":telephone,"CountryCode":CountryCode
        }
        respons = requests.get(url=url,params=params,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
    
    def get_countries(self, api_key: str) -> list:
        '''get countries

        Args:
            api_key (str): api key

        Returns:
            list: lsit of countries
        '''
        endpoint = "Phone/Countries"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        respons = requests.get(url=url,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        return respons.status_code