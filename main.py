import function

function.hello()
print()
function.what_your_type_password()
type_of_password = input("Please, write your type of password or commands: ")

while True:
    if type_of_password == '/wtp':
        print(function.about_types_of_password())
        type_of_password = input("Please, write your type of password or commands: ")
    elif type_of_password in ['1', '2', '3', '4']:
        password = function.choice_type_password(int(type_of_password))
        print()
        print("Your password: " + password)
        break
    else:
        type_of_password = input("You can write only numbers! Please, write your type of password again: ")

