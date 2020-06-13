import vk_api
import time

print("Скрипт для накрутки СМС! ")
print("Создатель: vk.com/chmotie \n Группа https://vk.com/scripts_xxx")
print("По вопросам писать в ЛС группы.")
print("Что бы продолжить пиши 1")


vibor = input("-->")
chelo = input("Введите ID первого человека который будет в беседе:")
chels = input("Введите ID первого человека который будет в беседе:")
tokene = input("Введите токен от кого будет создаваться беседа")	
kalas = input("Кол-во смс: ")
vk_session = vk_api.VkApi(token=tokene)
vk = vk_session.get_api()
chelii = [chelo,chels]
sdss = 0
while int(sdss) < int(kalas):
   try:
	   vk.messages.createChat(user_ids=chelii,title='pizdatya nakrutka chmotie')
	   sdss += 1
	   time.sleep(60)
   except vk_api.exceptions.ApiError:
       print("Чет не так Error 444")
