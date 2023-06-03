import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
BOT_TOKEN: str = '6171738053:AAFUuJtnCfJw9GnuhdG0DAZpGEVTBB0mzl4'
TEXT1: str = 'Все говорят: "'
TEXT2: str = '". \nА ты возьми и купи слона!'
MAX_COUNTER: int = 100

def start_bot():
    offset: int = -2
    counter: int = 0
    chat_id: int
    first_name: str
    message: str

    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    while not updates['result']:
        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
        time.sleep(5)

    first_name = updates['result'][-1]['message']['from']['first_name']
    chat_id = updates['result'][-1]['message']['from']['id']
    offset = updates['result'][-1]['update_id']

    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text="Привет, {first_name}!"')
    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text="Купи слона!"')

    while counter < MAX_COUNTER:
        print('request #', counter)
        updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
        if updates['result']:
            for result in updates['result']:
                chat_id = result['message']['from']['id']
                offset = result['update_id']
                message = TEXT1 + result['message']['text'] + TEXT2
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={message}')
        time.sleep(1)
        counter += 1
    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text="Я устал тебя уговаривать. \nПойду поем.\nПока!"')





if __name__ == '__main__':
    start_bot()

