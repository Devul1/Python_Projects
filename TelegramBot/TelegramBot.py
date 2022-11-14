import telebot
from config import TOKEN, values
from extensions import ConvertionException, ValuesConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome_help(message):
    instruction = 'Чтобы работать с ботом, нужно ввести команду следующего формата:\n\
<имя валюты> <в какую валюту переводить> <количество переводимой валюты>\n\
Увидеть список всех валют: /values'
    bot.send_message(message.chat.id, instruction)


@bot.message_handler(commands=['values'])
def values_list(message):
    text = 'Доступные валюты:'

    for key in values.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message):
    try:
        values_text = message.text.split(' ')

        if len(values_text) != 3:
            raise ConvertionException('Введите 3 параметра!')

        base, quote, amount = values_text
        total_base = ValuesConverter.get_price(base, quote, amount)
    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {base} в {quote} = {total_base}'
        bot.reply_to(message, text)


bot.polling(none_stop=True)
