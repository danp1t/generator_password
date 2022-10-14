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
    
If you specify your character set as a library, then its length must be at least 5 characters. P.S. You can repeat characters to get the length you want.
For example: 124 or 12453k!
                  
Please, enter libraries numbers: """)
            if not(0 < size_password <= 50):
                '1' + 2
            password = generator.create_own_password(size_password, libraties)
            print()
            print("Your password: " + password)
            break

        except:
            print("Error. Please, start again!")

    else:
        type_of_password = input("You can write only numbers! Please, write your type of password again: ")

