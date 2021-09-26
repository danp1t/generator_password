key = input("Введите ключ: ")

#Расшифровка ключа
#Расшифровка подсказки
prompt_len = len(key) - 4 - 12
prompt = key[2:(prompt_len + 2)]
alhabet_full = """1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@.#$%^&*()_+=-[]{}:;"',/?\|<>№~"""
new_prompt = ''
prompt = list(prompt)
for i in prompt:
    new_prompt = new_prompt + alhabet_full[alhabet_full.index(i) - 4]
print("Ваша подсказка:", new_prompt)

#Расшифровка индексов ключа
index_full = list(key[-14:-2])
index_first = index_full[7] + index_full[0] + index_full[5] + index_full[2]
index_second = index_full[8] + index_full[3] + index_full[10] + index_full[9]
index_first = "0x" + str(index_first)
index_second = "0x" + str(index_second)
index_first = int(index_first, base=16)
index_second = int(index_second, base=16)

#Расшифровка конца пароля
last_password = index_full[6] + index_full[1] + index_full[4] + index_full[11]

#Поиск пароля
text_password = open('text_password.txt', 'r')
password = text_password.read()[index_first:(index_second)]
if last_password in password:
    print('Ваш пароль:', password)
else:
    print("Ключ не подходит")



