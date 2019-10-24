import vk_api
import requests
import os
import time
from vk_api.longpoll import VkLongPoll, VkEventType

session = requests.Session()
login = '79996237427'
with open(os.path.join(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0], ".pswd")) as fd:
	password = fd.read()
vk_session = vk_api.VkApi(login, password, scope=140488159)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)

print(vk_session.get_api())
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
   #Слушаем longpoll, если пришло сообщение то:			
        if event.text == 'Первый вариант фразы' or event.text == 'Второй вариант фразы': #Если написали заданную фразу
            if event.from_user: #Если написали в ЛС
                vk.messages.send( #Отправляем сообщение
                    user_id=event.user_id,
                    message='Ваш текст'
		)
            elif event.from_chat: #Если написали в Беседе
                vk.messages.send( #Отправляем собщение
                    chat_id=event.chat_id,
                    message='Ваш текст'
		)

# def write_msg(user_id, message):
#     vk.method('messages.send', {'user_id': user_id, 'message': message})

# # API-ключ созданный ранее
# token = "98ed16d57f7707982de9e37d47558d290214cc900efe8471115a32757d04aef72690fe579fca4d106953b"

# # vk_session = vk_api.VkApi( login="TYPE_LOGIN_HERE", password="TYPE_PASSWORD_HERE", scope=140488159 )

# # Авторизуемся как сообщество
# vk = vk_api.VkApi(token=token)

# # Работа с сообщениями
# longpoll = VkLongPoll(vk)

# # Основной цикл
# for event in longpoll.listen():

#     # Если пришло новое сообщение
#     if event.type == VkEventType.MESSAGE_NEW:
    
#         # Если оно имеет метку для меня( то есть бота)
#         if event.to_me:
        
#             # Сообщение от пользователя
#             request = event.text
            
#             # Каменная логика ответа
#             if request == "привет":
#                 write_msg(event.user_id, "Хай")
#             elif request == "пока":
#                 write_msg(event.user_id, "Пока((")
#             else:
#                 write_msg(event.user_id, "Не поняла вашего ответа...")