import config, random

alhabet = ''
x = 1

#Входные данные (длина пароля и критерии)
length = int(input("Введите длину пароля: "))
while x != 0:
    criterions = input("""Введите цифрами критерии: 
    1. Цифры (123)
    2. Строчные буквы (abc)
    3. Прописные буквы (ABC)
    4. Специальные символы (;:#) 
Мои критерии: """)

    for i in criterions:
        if (i == '1') or (i == '2') or (i == '3') or (i == '4'):
            x = 0
        else:
            print("Произошла ошибка, попробуйте ещё раз")
while x == 0:
    prompt = input("Введите подсказку: ")
    a = 0
    for i in prompt:
        if i in ['<', '>', '№', '~']:
            print("Подсказка содержит недопустимые знаки")
            a += 1
    if a == 0:
        x = 1

alhabet_full = config.numbers_alhabet + config.str_alhabet + config.pro_alhabet + config.spec_alhabet
new_prompt = ''
prompt = list(prompt)
for i in prompt:
    new_prompt = new_prompt + alhabet_full[alhabet_full.index(i) + 4]




#Формирование алфавита
for i in criterions:
    if i == '1':
        alhabet += config.numbers_alhabet
    elif i == '2':
        alhabet += config.str_alhabet
    elif i == '3':
        alhabet += config.pro_alhabet
    elif i == '4':
        alhabet += config.spec_alhabet

#Генерирование тестового файла
password = ''
while len(password) != 50000:
    password += random.choice(alhabet)
text_password = open('text_password.txt', 'w')
text_password.write(password)
text_password.close()

#Формирование пароля
text_password = open('text_password.txt', 'r')
x = (text_password.read())
index_first = random.randint(5000, 50000)
index_second = -1
while len(x[index_first:index_second]) != length:
    index_second = random.randint(0, 50000)
print('Ваш пароль:', x[index_first:index_second])
last_words = x[index_first:index_second]
last_words = last_words[-1:-5:-1]
last_words = last_words[::-1]
text_password.close()


#Генерирование ключа
index_first = hex(index_first)[::-1]
index_first = index_first[0:4]
index_first = index_first[::-1]

index_second = hex(index_second)[::-1]
index_second = index_second[0:4]
index_second = index_second[::-1]

key = "--" + new_prompt + index_first[1] + last_words[1] + index_first[3] \
      + index_second[1] + last_words[2] + index_first[2] \
      + last_words[0] + index_first[0] + index_second[0] \
      + index_second[3] + index_second[2] + last_words[3] + "--"

print("Ваш ключ:", key)





