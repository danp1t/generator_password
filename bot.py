import telebot
import pymysql
import time
from config import host, user, password, db_name, TOKEN

bot = telebot.TeleBot(TOKEN)


def read_table():
    connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name,
                                 cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        select_all_rows = "SELECT * FROM `info_user`"
        cursor.execute(select_all_rows)
        rows = cursor.fetchall()
        connection.close()
        return rows


@bot.message_handler(commands=["start"])
def welcome(message):
    id_list = []
    for i in read_table():
        id_list.append(i['user_id'])
    if message.from_user.id not in id_list:
        connection = pymysql.connect(host=host, port=3306, user=user, password=password, database=db_name,
                                     cursorclass=pymysql.cursors.DictCursor)
        user_id = message.from_user.id
        if message.from_user.username != None:
            user_name = message.from_user.username
        elif message.from_user.last_name != None:
            user_name = str(message.from_user.first_name) + " " + str(message.from_user.last_name)
        else:
            user_name = message.from_user.first_name
        first_date = time.strftime('%Y-%m-%d')

        with connection.cursor() as cursor:
            insert_query = "INSERT INTO `info_user` (user_id, user_name, first_date) VALUES ({0}, '{1}', '{2}');".format(
                user_id, user_name, first_date)
            cursor.execute(insert_query)
            connection.commit()
            connection.close()
        bot.send_message(message.chat.id, """Привет, <b>{0}</b>. Меня зовут - <b>Гена</b>. Давай, я немного расскажу о себе.

Я умею генерировать пароли, но не как все. Однако, алгоритм я тебе не расскажу, прости. В отличие от других ботов, я предоставляю следующие возможности:

1. Я буду давать тебе ключ для доступа к паролю. Это позволит тебе оставить подсказку для своего пароля.
2. Я буду напоминать о том, чтобы ты обновлял пароли каждый месяц. Буду отправлять тебе напоминание на почту (если она будет указана в твоем профиле) и в этот чат.
3. Я позволяю выставлять критерии для генерирование пароля.

Сейчас, я предлагаю тебе перейти к настройке профиля.


""".format(user_name), parse_mode='html')
        # Отправить сообщение для настройки профиля user'а


    else:
        bot.send_message(message.chat.id, """Привет! Меня зовут - <b>Гена</b>. Давай, я немного расскажу о себе.

Я умею генерировать пароли, но не как все. Однако, алгоритм я тебе не расскажу, прости. В отличие от других ботов, я предоставляю следующие возможности:

1. Я буду давать тебе ключ для доступа к паролю. Это позволит тебе оставить подсказку для своего пароля.
2. Я буду напоминать о том, чтобы ты обновлял пароли каждый месяц. Буду отправлять тебе напоминание на почту (если она будет указана в твоем профиле) и в этот чат.
3. Я позволяю выставлять критерии для генерирование пароля.

Сейчас, я предлагаю тебе перейти к настройке профиля.


""", parse_mode='html')
        # Отправить сообщение для настройки профиля user'а")


if __name__ == '__main__':
    bot.polling(none_stop=True)