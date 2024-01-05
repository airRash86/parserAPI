



import telebot
from telebot import types
import requests

#t.me/ANY_TESTS_123_BOT
bot = telebot.TeleBot('6199105654:AAGs8Bg7cBlBP2k9DiCrDT3KlYz41S62uzU')

def change_TagsFunc(TXT):
    dicForchange_Tags = {
            "<li> <p>": '\n-',
            "<p>": '\n',
            "<strong>": '<b>',
            "</strong>": '</b>',
            "</p>": '',
            "<em>": '',
            "</em>": '',
            "<br />": '\n',
            "<ul>": '',
            "<li>": '\n-',
            "</li>": '',
            "</ul>": ''
            }
    for key, value in dicForchange_Tags.items():
        TXT = TXT.replace(key, value)
        
    return TXT

# Отправляем размеченное сообщение
@bot.message_handler(content_types=['text'])
def send_Tagged_message(message):
##    Tagged_message = "Привет! Этот текст содержит различные теги:\n" \
##                     "<b>Жирный текст</b>, <i>Курсив</i>, <code>Моноширинный текст</code>"

##    Tagged_message = '<p>Мы частная научная лаборатория, с 2019 года работаем над созданием технологии искусственного сознания, которая позволяет ИИ осмысливать сгенерированные в диалоге с человеком данные, понимать и прогнозировать индивидуальное эмоциональное состояние и поведение человека. Команда занимается реализацией технологии, прототип завершен (TRL 5). Mvp станет виртуальный собеседник [I.am], способный пройти тест Тьюринга.</p> <p><strong>Обязанности:</strong></p> <ul> <li>реализовывать алгоритмы и структуры данных для решения задач на графах;</li> <li>оптимизировать и рефакторить существующий код;</li> <li>разрабатывать прототипы для проверки гипотез, связанных с обработкой текста.</li> </ul> <p><strong>Требования:</strong></p> <ul> <li>уверенное использование Python 3.8;</li> <li>знание базовых структур данных и алгоритмов, способность оценивать скорость работы алгоритмов;</li> <li>умение вникать в большие объемы кода,</li> <li>знание основ Git;</li> <li>психологическая зрелость, высокий уровень самостоятельности.</li> </ul> <p><strong>Условия:</strong></p> <ul> <li> <p><strong><em>работа в офисе (в Москве или Ереване), 40 ч в неделю, </em></strong>возможен гибкий график;</p> </li> <li> <p>официальное трудоустройство;</p> </li> <li> <p>профессиональный рост на решении трендовой задачи;</p> </li> <li> <p>комфортный офис в БЦ «Тушино» (D2 «Трикотажная» / м. Тушинская).</p> </li> </ul> <p><em>В сопроводительном письме укажите ссылку на github или выполненное тестовое задание, которое можно решить по ссылке: </em><em>https://drive.google.com/file/d/1yJSslUMm4BRZdW4nFK3PITZLe04_ErNq/view </em></p> <p><em>В случае правильного решения теста, Вы будете приглашены сразу на финальное собеседование.</em></p>'
    buildNewVacancyBUTT = types.InlineKeyboardMarkup()
    showBUTT = types.InlineKeyboardButton(text = "Показать", callback_data = 'show_88925330')
    buildNewVacancyBUTT.add(showBUTT)
    bot.send_message(message.chat.id, 'Новая вакуха\n\
Показать подробности?', reply_markup=buildNewVacancyBUTT)


@bot.callback_query_handler(func = lambda call: True)
def ans(call):
    if 'show' in call.data:
##        print(call.data.split('_')[0], call.data.split('_')[1])
##        send_msg_NewPOST(LST_For_Topic[2], LST_For_Topic[1])
        
        response_1 = requests.get(F"https://api.hh.ru/vacancies/{call.data.split('_')[1]}")
        full_vacancy_data = response_1.json()
        Tagged_message = full_vacancy_data["description"]
    
        change_Tags = change_TagsFunc(Tagged_message)
##        bot.send_message(message.chat.id, change_Tags, parse_mode='HTML')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=change_Tags, parse_mode='HTML')
        
    bot.answer_callback_query(callback_query_id=call.id) #это чтобы иконка часов не висела на кнопке

# Запускаем обработчик сообщений
bot.polling()











