import requests
from .randommer import Randommer

class Finance(Randommer):
    def get_crypto_address_types(self, api_key: str) -> list:
        '''get available crypto types

        Args:
            api_key (str): api key

        Returns:
            list: list of types
        '''
        endpoint = "Finance/CryptoAddress/Types"
        url = self.get_url()+endpoint
        heards={
            "X-Api-Key": api_key
        }
        respons = requests.get(url,headers=heards)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
    def get_crypto_address(self,crypto_type:str, api_key: str) -> dict:
        '''get available crypto address

        Args:
            crypto_type (str): crypto type
            api_key (str): api key

        Returns:
            dict: crypto address
        '''

        endpoint = "Finance/CryptoAddress"
        url = self.get_url()+endpoint
        heards = {
            "X-Api-Key": api_key
        }
        paylod = {
            "cryptoType": crypto_type
        }
        respons = requests.get(url,params=paylod , headers=heards)
        if respons.status_code==200:
            return respons.json()
        return respons.status_code
        

    def get_countries(self, api_key: str) -> list:
        '''get available countries

        Args:
            api_key (str): api key

        Returns:
            list: crypto address
        '''
        endpoint = "Finance/Countries"
        url = self.get_url() + endpoint
        headers = {
            "X-Api-Key":api_key
        }
        respons = requests.get(url,headers=headers)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code


    def get_iban_by_country_code(self, country_code: str, api_key: str) -> dict:
        '''get available countries

        Args:
            country_code (str): country code
            api_key (str): api key

        Returns:
            dict: idan data
        '''
        endpoint = "Finance/Iban/"+f"{country_code}"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        params = {
            "countryCode":country_code
        }
        respons = requests.get(url,params=params,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code