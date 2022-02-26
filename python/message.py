import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from functions import function
from db import write_db
from settings import tokens




vk = vk_api.VkApi(token=tokens()[0])
longpoll = VkLongPoll(vk)


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,  'random_id': 0})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:

        if event.to_me:
            request = event.text

            if request == "привет":
                result = function(event.user_id)
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