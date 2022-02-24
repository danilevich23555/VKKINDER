import requests
import datetime
from settings import tokens



def get_VK_URL_user(owner_id):
    now = datetime.datetime.now()
    year_now = now.strftime("%Y")
    URL = 'https://api.vk.com/method/users.get'
    params = {
        'user_ids': owner_id,
        'access_token': tokens()[0],
        'v': '5.131',
        'fields': 'sex, bdate, city, country, home_town, relation'

    }
    resp = requests.get(URL, params=params)
    user_info = (resp.json()['response'][0])
    temp = []
    temp.append({'id': user_info['id'], 'first_name': user_info['first_name'],
                 'last_name': user_info['last_name'], 'sex': user_info['sex'],
                 'bdate': user_info['bdate'], 'city': user_info['city']['id'],
                 'year_old': (int(year_now) - int(user_info['bdate'][-4:]))})
    return temp

