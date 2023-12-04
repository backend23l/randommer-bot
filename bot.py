import requests
from settings import URL, API_KEY, card_msg
from time import sleep
from randommer.card import Card
from datetime import datetime


welcome_msg = '''
Hello and welcome to Randommer Bot!

🎉 Get ready for a diverse range of randomness with our exciting features. Here's a quick guide on how to use this bot:

1. /start: Use this command to receive a warm welcome message and get instructions on how to interact with the bot.

2. /card: Feeling lucky? Use this command to draw a random card and see what fortune it holds for you.

3. /finance: Looking for some crypto randomness? Type this command to get a random crypto address.

4. /misc: Explore the richness of various cultures! Use this command to receive information on 5 randomly selected cultures.

5. /name: Need a name on the spot? Type this command for a completely random full name.

6. /phone: If you're in need of phone numbers, use this command to get 5 randomly generated Uzbekistan phone numbers.

7. /social_number: Curious about social numbers? Use this command to get a randomly generated social number.

8. /text: Want some Lorem Ipsum text? Type this command to receive 20 words of normal Lorem Ipsum text.

9. /busywork: Need something to keep yourself occupied? Use this command for advice on productive and engaging tasks.'''


def get_last_update(url: str) -> dict:
    endpoint = '/getUpdates'
    url += endpoint
    
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()['result']

        if len(result) != 0:
            return result[-1]

        else:
            return 404
    
    return response.status_code

def send_message(url: str, chat_id: int, text: str, mode=False):
    endpoint = '/sendMessage'
    url += endpoint

    payload = {
        'chat_id': chat_id,
        'text': text
    }
    if mode:
        payload['parse_mode'] = 'HTML'

    requests.get(url, params=payload)


def main():
    c = Card()
    last_update_id = -1
    while True:
        curr_update = get_last_update(URL)

        if curr_update['update_id'] != last_update_id:
            user = curr_update['message']['from']
            text = curr_update['message'].get('text')

            if text is None:
                send_message(URL, user['id'], 'send text message')
            elif text == '/start':
                send_message(URL, user['id'], welcome_msg)
            elif text == '/card':
                card_data = c.get_card(api_key=API_KEY)
                date = datetime.fromisoformat(card_data['date'])
                msg = card_msg.format(
                    type=card_data['type'],
                    fullName=card_data['fullName'],
                    cardNumber=card_data['cardNumber'],
                    cvv=card_data['cvv'],
                    pin=card_data['pin'],
                    date=date.strftime("%Y-%m-%d")
                )
                send_message(URL, user['id'], msg, mode=True)
            else:
                send_message(URL, user['id'], 'error message')

            last_update_id = curr_update['update_id']

        sleep(0.5)

main()