import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from user import get_VK_URL_user
from find_users import filter_id
from db import write_db, select_count_id
from settings import tokens


vk = vk_api.VkApi(token=tokens()[0])
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': 0})



for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "подобрать пару":
                temp = select_count_id(event.user_id)
                if temp == [[]]:
                    counter = 0
                else:
                    counter = temp[0][0][1]
                user_info = get_VK_URL_user(event.user_id)
                city = user_info[0]['city']
                year_old = user_info[0]['year_old']
                sex = user_info[0]['sex']
                result = filter_id(city, year_old, sex, counter)
                if result == []:
                    while result == []:
                        counter = counter + 1
                        result = filter_id(city, year_old, sex, counter)
                a = ((result[0][0]['id_profile']))
                b = {a}
                if set(temp[1:])&b != set():
                    while set(temp[1:])&b != set():
                        counter = counter + 1
                        result = filter_id(city, year_old, sex, counter)
                        if result == []:
                            pass
                        else:
                            a = ((result[0][0]['id_profile']))
                            b = {a}
                for line in range(len(result)):
                    if len(result[line]) == 2:
                        write_db(event.user_id, result[line][0]['id_profile'], result[line][0]['url_profile'],
                                 result[line][0]['url_photo'], result[line][1]['url_photo'],
                                 None)
                        write_msg(event.user_id, f"Профайл: \n {result[line][0]['url_profile']} \n Фото: "
                                                 f"\n {result[line][0]['url_photo']}, \n {result[line][1]['url_photo']}")
                    elif len(result[line]) == 1:
                        write_db(event.user_id, result[line][0]['id_profile'], result[line][0]['url_profile'],
                             result[line][0]['url_photo'], None, None)
                        write_msg(event.user_id, f"Профайл: \n {result[line][1]['url_profile']} \n Фото: "
                                                 f"\n {result[line][0]['url_photo']}")

                    elif len(result[line]) == 0:
                        pass
                    else:
                        write_db(event.user_id, result[line][1]['id_profile'], result[line][1]['url_profile'],
                                 result[line][0]['url_photo'], result[line][1]['url_photo'],
                                 result[line][2]['url_photo'])
                        write_msg(event.user_id, f"Профайл: \n {result[line][0]['url_profile']} \n Фото: "
                                                 f"\n {result[line][0]['url_photo']}, \n {result[line][1]['url_photo']}, "
                                                 f"\n " f"{result[line][2]['url_photo']}")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")