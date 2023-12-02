import requests
from .randommer import Randommer


class SocialNumber(Randommer):
    def get_SocialNumber(self, api_key: str) -> str:
        '''get SocialNumber

        Args:
            api_key (str): api key

        Returns:
            str: number as str
        '''
        endpoint = "SocialNumber"
        url = self.get_url() + endpoint
        headrs = {
            "X-Api-Key":api_key
        }
        respons = requests.get(url=url,headers=headrs)
        if respons.status_code==200:
            return respons.json()
        return respons.status_code