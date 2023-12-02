import requests
from .randommer import Randommer


class Text(Randommer):
    def generate_LoremIpsum(self, api_key: str, loremType: str, type: str, number: int) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            loremType (str): loremType (normal or bussines)
            type (str): type (words or paragraphs)
            number (int): number

        Returns:
            str: Lorem text
        '''
        endpoint = "Text/LoremIpsum"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        params = {
            "loremType":loremType,"type":type,"number":number
        }
        respons = requests.get(url=url,params=params,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
    
    def generate_password(self, api_key: str, length: int, hasDigits: bool, hasUppercase: bool, hasSpecial: bool) -> str:
        '''Generate lorem ipsum

        Args:
            api_key (str): api key
            length (int): lenth of password
            hasDigits (bool): hasDigits
            hasUppercase (bool): hasUppercase
            hasSpecial (bool): hasSpecial

        Returns:
            str: pasword
        '''
        endpoint = "Text/LoremIpsum"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        params = {
            "length":length,"hasDigits":hasDigits,"hasUppercase":hasUppercase,"hasSpecial":hasSpecial
        }
        respons = requests.get(url=url,params=params,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        else:
            return respons.status_code
