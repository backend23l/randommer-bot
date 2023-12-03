from settings import url,api_key
import requests
from randommer.card import Card
from randommer.finance import Finance
from randommer.misc import Misc
from randommer.name import Name
from randommer.phone import Phone
from randommer.socialnumber import SocialNumber
from randommer.text import Text
from time import sleep
mseg = '''
    <b>Hello and welcome to Randommer Bot!</b>

🎉 Get ready for a diverse range of randomness with our exciting features. Here's a quick guide on how to use this bot:

1. /start: Use this command to receive a warm welcome message and get instructions on how to interact with the bot.

2. /card: Feeling lucky? Use this command to draw a random card and see what fortune it holds for you.

3. /finance: Looking for some crypto randomness? Type this command to get a random crypto address.

4. /misc: Explore the richness of various cultures! Use this command to receive information on 5 randomly selected cultures.

5. /name: Need a name on the spot? Type this command for a completely random full name.

6. /phone: If you're in need of phone numbers, use this command to get 5 randomly generated Uzbekistan phone numbers.

7. /social_number: Curious about social numbers? Use this command to get a randomly generated social number.

8. /text: Want some Lorem Ipsum text? Type this command to receive 20 words of normal Lorem Ipsum text.

'''
def echoobot_updets(url:str):
    endpoint = "/getUpdates"
    url+=endpoint
    respons = requests.get(url)
    if respons.status_code==200:
        result = respons.json()["result"]
        if len(result)!=0:
            return result[-1]
        else:
            return 404
    else:
        return respons.status_code
print(echoobot_updets(url))
def send_message(url:str,chat_id:int,text:str):
    endpoint = "/sendMessage"
    url+=endpoint
    payload = {
        "chat_id":chat_id,
        "text":text,
        "parse_mode":"HTML"
    }
def main(url:str):
    last_update_id = -1 
    card = Card()
    finance = Finance()
    misc = Misc()
    name = Name()
    phone = Phone()
    socialnumber = SocialNumber()
    word = Text()
    while True:
        curer_update = echoobot_updets(url)
        if curer_update['update_id']!=last_update_id:
            user = curer_update['message']['from']
            text = curer_update['message'].get('text')
            if text is None:
                send_message(url,user['id'],"Menga text xabar yuboring !!!")
            elif text == "/start":
                send_message(url,user['id'],mseg)
            elif text == "/card":
                advic_car = card.get_card(api_key)['cardNumber']
                send_message(url,user['id'],advic_car)
            elif text=="/finance":
                crypto_type = "Argoneum"
                advic_finc = finance.get_crypto_address(crypto_type,api_key)['address']
                send_message(url,user['id'],advic_finc)
            elif text == "/misc":
                number = 5
                advic_misc = misc.get_random_address(api_key=api_key,number=number,culture="en")
                send_message(url,user['id'],advic_misc)
            elif text == "/name":
                quantitiy = 1
                nametype = "fullname"
                advic_name = name.get_name(api_key=api_key,nameType=nametype,quantity=quantitiy)
                send_message(url,user['id'],advic_name)
            elif text == "/phone":
                countrycode = "US"
                soni = 5
                advic_phon = phone.generate(api_key=api_key,CountryCode=countrycode,Quantity=soni)
                send_message(url,user['id'],advic_phon)
            elif text == "/social_number":
                advic_social = socialnumber.get_SocialNumber(api_key=api_key)
                send_message(url,user['id'],advic_social)
            elif text == "/text":
                loremtype = "normal"
                type = "words"
                number = 20
                advic_text = word.generate_LoremIpsum(api_key=api_key,loremType=loremtype,type=type,number=number)
                send_message(url,user['id'],advic_text)
            else:
                send_message(url,user['id'],"Hato ma'lumot yuborildi !!!")
            last_update_id = curer_update['update_id']
        sleep(0.5)
main(url)
            
            


