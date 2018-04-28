import requests
from time import sleep

url = "https://api.telegram.org/bot582749012:AAFk3Tl0SnvJ2_XC5JY-CeFEtiA30oB-CBQ/"

# api.telegram возвращает информацию в формате JSON. 



# Функция getUpdates возвращает все обновления за последние 24 часа. 
# Словарь обновления состоит из двух частей: ok и result.
# В функции get_updates_json параметр сдвига offset помечает просмотренные обновления.
def get_updates_json(request):  
    params = {'timeout': 100, 'offset': None}
    response = requests.get(request + 'getUpdates', data=params)
    return response.json()

def last_update(data):  
    results = data['result']
    total_updates = len(results) - 1
    return results[total_updates]

# Функция get_chat_id изымает из обновление id чата.     
def get_chat_id(update):  
    chat_id = update['message']['chat']['id']
    return chat_id    

# Функция send_mess отправляет текстовое сообщение в чат.
def send_mess(chat, text):  
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response     

 

def main():  
    update_id = last_update(get_updates_json(url))['update_id']
    your_massage = 'text'   
    while True:
        if update_id == last_update(get_updates_json(url))['update_id']:
           send_mess(get_chat_id(last_update(get_updates_json(url))), your_massage)
           update_id += 1
        sleep(1)       

if __name__ == '__main__':  
    main()

#class PyBot:

# token - токен, полученный при регистрации бота.
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

# Функция getUpdates возвращает все обновления за последние 24 часа. 
# Словарь обновления состоит из двух частей: ok и result.
# В функции get_updates_json параметр сдвига offset помечает просмотренные обновления.
   def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

        

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
        
# last_update - функция для получения последнего обновления.        
    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update       