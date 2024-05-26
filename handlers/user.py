import telebot
from telebot.handler_backends import StatesGroup, State

from funcs.datatime import gel_welcome
from funcs.db import get_institute_from_db
from funcs.functionality import functionality
from funcs.functionality2 import functionality2
from init_bot import bot


# class UserState(StatesGroup):
#     state1 = State()


@bot.message_handler(commands=["start", "help"])
def start(message: telebot.types.Message):
    text = f"{gel_welcome()} \n" \
           f"Я бот-помощник для университета🏛\n\n" \
           f"Вот что я имею:\n" \
           f"{functionality()}"
    bot.send_message(message.chat.id, text)
    # bot.set_state(message.from_user.id, UserState.state1)


# state=UserState.state1
@bot.message_handler(commands=["get_info"])
def get_info(message: telebot.types.Message):
    text = f"Чем я могу помочь?👩🏻‍🎓\n" \
           f"{functionality2()}"
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=["get_university"])
def get_university(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Сайт": {"url": "https://www.nntu.ru/content/universitet/rukovodstvo"}
    })
    bot.reply_to(message, "Вот необходимая информация о высшем руководстве:  ", reply_markup=markup)


@bot.message_handler(commands=["get_directorate"])
def get_directorate(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=2)
    markup.add(
        telebot.types.KeyboardButton("ИРИТ"),
        telebot.types.KeyboardButton("ИТС"),
        telebot.types.KeyboardButton("ИФХТиМ"),
        telebot.types.KeyboardButton("ИНЭЛ"),
        telebot.types.KeyboardButton("ИЯЭиТФ"),
        telebot.types.KeyboardButton("ИПТМ"),
        telebot.types.KeyboardButton("ИНЭУ")

    )
    bot.reply_to(message, "Информацию о дирекции какого института Вам нужно предоставить?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "ИРИТ")
def handle_action(message: telebot.types.Message):
    institutes = get_institute_from_db(message.text)
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/irit_official"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/irit"},
        "Местоположение": {"url": "https://yandex.ru/maps/-/CDbp4-yv"}
    })
    if not institutes:
        bot.send_message(message.chat.id, "Нет информации о институте")
    else:
        for idx, institute in enumerate(institutes):
            bot.send_message(message.chat.id, f"Информация о выбранном институте: \n"
                                              f"Название института: {institute[1]}\n"
                                              f"Директор института: {institute[2]}\n"
                                              f"Номер дирекции: {institute[3]}\n"
                                              f"Почта дирекции: {institute[4]}\n"
                                              f"Адрес: {institute[5]}\n\n"
                                              f"Вот необходимые ссылки о дирекции ИРИТ: ",
                             parse_mode="HTML", reply_markup=markup)

            bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
            bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИТС")
def handle_action(message: telebot.types.Message):
    institutes = get_institute_from_db(message.text)
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/its_ngtu"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/its"},
        "Местоположение": {"url": "https://yandex.ru/maps/-/CDbpIR69"}
    })
    if not institutes:
        bot.send_message(message.chat.id, "Нет информации о институте")
    else:
        for idx, institute in enumerate(institutes):
            bot.send_message(message.chat.id, f"Информация о выбранном институте: \n"
                                              f"Название института: {institute[1]}\n"
                                              f"Директор института: {institute[2]}\n"
                                              f"Номер дирекции: {institute[3]}\n"
                                              f"Почта дирекции: {institute[4]}\n"
                                              f"Адрес: {institute[5]}\n\n"
                                              f"Вот необходимые ссылки о дирекции ИРИТ: ",
                             parse_mode="HTML", reply_markup=markup)

            bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
            bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИФХТиМ")
def handle_action(message: telebot.types.Message):
    institutes = get_institute_from_db(message.text)
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/ifhtim"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/ifhtim"},
        "Местоположение": {"url": "https://yandex.ru/maps/-/CDbpIO1i"}
    })
    if not institutes:
        bot.send_message(message.chat.id, "Нет информации о институте")
    else:
        for idx, institute in enumerate(institutes):
            bot.send_message(message.chat.id, f"Информация о выбранном институте: \n"
                                              f"Название института: {institute[1]}\n"
                                              f"Директор института: {institute[2]}\n"
                                              f"Номер дирекции: {institute[3]}\n"
                                              f"Почта дирекции: {institute[4]}\n"
                                              f"Адрес: {institute[5]}\n\n"
                                              f"Вот необходимые ссылки о дирекции ИРИТ: ",
                             parse_mode="HTML", reply_markup=markup)

            bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
            bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИНЭЛ")
def handle_action(message: telebot.types.Message):
    institutes = get_institute_from_db(message.text)
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/inel_ngtu"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/inel"},
        "Местоположение": {"url": "https://yandex.ru/maps/-/CDbpI005"}
    })
    if not institutes:
        bot.send_message(message.chat.id, "Нет информации о институте")
    else:
        for idx, institute in enumerate(institutes):
            bot.send_message(message.chat.id, f"Информация о выбранном институте: \n"
                                              f"Название института: {institute[1]}\n"
                                              f"Директор института: {institute[2]}\n"
                                              f"Номер дирекции: {institute[3]}\n"
                                              f"Почта дирекции: {institute[4]}\n"
                                              f"Адрес: {institute[5]}\n\n"
                                              f"Вот необходимые ссылки о дирекции ИРИТ: ",
                             parse_mode="HTML", reply_markup=markup)

            bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
            bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИЯЭиТФ")
def handle_action(message: telebot.types.Message):
    institutes = get_institute_from_db(message.text)
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/nnstu_ftf"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/iyaeitf"},
        "Местоположение": {"url": "https://yandex.ru/maps/-/CDbpIDzs"}
    })
    if not institutes:
        bot.send_message(message.chat.id, "Нет информации о институте")
    else:
        for idx, institute in enumerate(institutes):
            bot.send_message(message.chat.id, f"Информация о выбранном институте: \n"
                                              f"Название института: {institute[1]}\n"
                                              f"Директор института: {institute[2]}\n"
                                              f"Номер дирекции: {institute[3]}\n"
                                              f"Почта дирекции: {institute[4]}\n"
                                              f"Адрес: {institute[5]}\n\n"
                                              f"Вот необходимые ссылки о дирекции ИРИТ: ",
                             parse_mode="HTML", reply_markup=markup)

            bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
            bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИПТМ")
def handle_action(message: telebot.types.Message):
    institutes = get_institute_from_db(message.text)
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/ngtuiptm"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/iptm"},
        "Местоположение": {"url": "https://yandex.ru/maps/-/CDbpIH9D"}
    })
    if not institutes:
        bot.send_message(message.chat.id, "Нет информации о институте")
    else:
        for idx, institute in enumerate(institutes):
            bot.send_message(message.chat.id, f"Информация о выбранном институте: \n"
                                              f"Название института: {institute[1]}\n"
                                              f"Директор института: {institute[2]}\n"
                                              f"Номер дирекции: {institute[3]}\n"
                                              f"Почта дирекции: {institute[4]}\n"
                                              f"Адрес: {institute[5]}\n\n"
                                              f"Вот необходимые ссылки о дирекции ИРИТ: ",
                             parse_mode="HTML", reply_markup=markup)

            bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
            bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(func=lambda message: message.text == "ИНЭУ")
def handle_action(message: telebot.types.Message):
    institutes = get_institute_from_db(message.text)
    markup = telebot.util.quick_markup({
        "Группа в ВК": {"url": "https://vk.com/ineungtu"},
        "Сайт": {"url": "https://www.nntu.ru/structure/view/podrazdeleniya/ineu"},
        "Местоположение": {"url": "https://yandex.ru/maps/-/CDbpILl8"}
    })
    if not institutes:
        bot.send_message(message.chat.id, "Нет информации о институте")
    else:
        for idx, institute in enumerate(institutes):
            bot.send_message(message.chat.id, f"Информация о выбранном институте: \n"
                                              f"Название института: {institute[1]}\n"
                                              f"Директор института: {institute[2]}\n"
                                              f"Номер дирекции: {institute[3]}\n"
                                              f"Почта дирекции: {institute[4]}\n"
                                              f"Адрес: {institute[5]}\n\n"
                                              f"Вот необходимые ссылки о дирекции ИРИТ: ",
                             parse_mode="HTML", reply_markup=markup)

            bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
            bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(commands=["get_lk"])
def get_lk(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Личный кабинет": {
            "url": "https://auth.nntu.ru/idp/oauth2_login.jsp#/provider/LDAP/12ef96388641343f28b7d5bd10cf430e"}
    })
    text = "Личный кабинет студент позволит вам иметь доступ к информации об учебном планирование и успеваемости.\n\n"
    bot.send_message(message.chat.id, f"{text}Вот ссылка на личный кабинет учащегося НГТУ им. Р.Е.Алексеева:", reply_markup=markup)
    # bot.reply_to(message, "Вот ссылка на личный кабинет учащегося/сотрудника НГТУ им. Р.Е.Алексеева:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)


@bot.message_handler(commands=["get_url"])
def get_url(message: telebot.types.Message):
    markup = telebot.util.quick_markup({
        "Сайт университета": {"url": "https://www.nntu.ru/"}
    })
    bot.reply_to(message, "Вот ссылка на сайт НГТУ им. Р.Е.Алексеева:", reply_markup=markup)
    bot.send_message(message.chat.id, f"Выберете следующий шаг:\n{functionality2()}")
    bot.clear_reply_handlers_by_message_id(message.message_id)

# state=UserState.state1
@bot.message_handler(commands=["end"])
def end(message: telebot.types.Message):
    markup = telebot.types.ReplyKeyboardRemove()
    text = f"Спасибо! Пока)"
    bot.send_message(message.chat.id, text, reply_markup=markup)
    # bot.delete_state(message.from_user.id)
