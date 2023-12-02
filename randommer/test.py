from card import Card
from finance import Finance
from misc import Misc
from name import Name
from phone import Phone
from socialnumber import SocialNumber
from text import Text
token = '2d794c6f46094ceb96bd719c1c26c984'


card = Card()
print(card.get_card_types(api_key=token))

# print(card.get_card(api_key=token))

financ = Finance()
# print(financ.get_crypto_address_types(token))

crypto_type = "Argoneum"
# print(financ.get_crypto_address(crypto_type=crypto_type,api_key=token))

# print(financ.get_countries(api_key=token))

country_code = "BG"
# print(financ.get_iban_by_country_code(country_code=country_code,api_key=token))

misc = Misc()
# print(misc.get_cultures(token))

number = "132"
culture = "en"
# print(misc.get_random_address(api_key=token,number=number,culture=culture))

name = Name()
namtype = "fullname"
quantity = 5
# print(name.get_name(api_key=token,nameType=namtype,quantity=quantity))

strartingwords = "Salom "
# print(name.get_name_suggestions(api_key=token,startingWords=strartingwords))

# print(name.get_name_cultures(api_key=token))

phone = Phone()
countrycode = "US"
soni = 5
# print(phone.generate(api_key=token,CountryCode=countrycode,Quantity=soni))

phone_numbers = 10
# print(phone.get_IMEI(api_key=token,Quantity=phone_numbers))

validcountrycode = "uz"
telephone = "+998 938554640"
# print(phone.is_valid(api_key=token,CountryCode=validcountrycode,telephone=telephone))

# print(phone.get_countries(api_key=token))
socialnumber = SocialNumber()
# print(socialnumber.get_SocialNumber(api_key=token))

text = Text()
loremtype = "normal"
type = "paragraphs"
number = 2
# print(text.generate_LoremIpsum(api_key=token,loremType=loremtype,type=type,number=number))

len = 8
true = True
false = False
hasdigit = true
hasupper = true
hasspecial = false
print(text.generate_password(api_key=token,length=len,hasDigits=hasdigit,hasUppercase=hasupper,hasSpecial=hasspecial))
