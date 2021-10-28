import random
import telebot
from telebot import types

bot = telebot.TeleBot('2051154474:AAF1Xif4JWpuqRCSr_fALkGFV-2upSNuuOs')

# Заготовки для трёх предложений
first = ['Естественно, прости, что так редко говорю', 'Разумеется, именно поэтому я создал бота, чтобы не забывать тебе это говорить', 'Да, и сильно скучаю']
second = ['Ты пахнешь как любовь', 'Ты сумасшествие с первого взгляда', 'Ты пахнешь шоколадом', 'Пахнешь, как цветы', 'Пахнешь как мечты', 'Пахнешь, как желание, чистое животное желание.', 'Но ты пахнешь на шестнадцать, ты как первое свидание.', ]
# Метод, который получает сообщения и обрабатывает их



@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Хрю':

        keyboard = types.InlineKeyboardMarkup()

        key_love = types.InlineKeyboardButton(text='Люблю ли я Дашу?', callback_data='love')
        keyboard.add(key_love)

        key_btfl = types.InlineKeyboardButton(text='Дашка у меня красивая?', callback_data='btfl')
        keyboard.add(key_btfl)
        bot.send_message(message.from_user.id, text='Я не сомневался, что ты отгадаешь пароль. А здесь ответы на самые важные в мире вопросы', reply_markup=keyboard)

    else:
        bot.send_message(message.from_user.id, "Введите свинячий пароль")




# Обработчик нажатий на кнопки
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "love":
        msg = random.choice(first)
        bot.send_message(call.message.chat.id, msg)
    elif call.data == "btfl":
        msg = random.choice(second)
        bot.send_message(call.message.chat.id, msg)

bot.polling(none_stop=True, interval=0)

