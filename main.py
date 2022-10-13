import function
import generator

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
    elif type_of_password == '5':
        try:
            size_password = int(input("Enter (numbers) password size (1-50): "))
            libraties = input("""Libraries:
    
    1) numbers (0123456789)
    2) low_english (zxcvbnmasdfghjklpoiuytrewq)
    3) upper_english (ZXCVBNMASDFGHJKLQWERTYUIOP)
    4) special symbols (,.<>?/}]{[+=-_)(*&^:%$;№\|~`)
    
For example: 124
                  
Please, enter libraries numbers: """)
            if len(libraties) > 4 or not(0 < size_password <= 50):
                '1' + 2
            password = generator.create_own_password(size_password, libraties)
            print()
            print("Your password: " + password)
            break

        except:
            print("Error. Please, start again!")

    else:
        type_of_password = input("You can write only numbers! Please, write your type of password again: ")

