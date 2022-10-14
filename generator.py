#Python libraries
import random

#libraries for generator (CONST)
low_english = "zxcvbnmasdfghjklpoiuytrewq"
upper_english = "ZXCVBNMASDFGHJKLQWERTYUIOP"
dec_numbers = '0123456789'
spec_chars = ",.<>?/}]{[+=-_)(*&^:%$;№\|~`"

def create_standart_password():
    """libraries = dec_number + low_english
    size password = 8"""

    libraries = dec_numbers + low_english
    password = ""
    for i in range(8): #Size password
        password += random.choice(libraries)

    return password

def create_password_phone():
    """library = dec_number
    size password = 6"""

    library = dec_numbers
    password = ''
    for i in range(6): #size password
        password += random.choice(library)

    return password

def create_difficult_password():
    """Library = dec_number + low_english + spec_chars
    size password = 12
    Must contain at least one special character and a number."""

    libraries = low_english + dec_numbers + spec_chars
    password = ''
    while True:
        for i in range(12):  # size password
            password += random.choice(libraries)

        flag1 = 0
        flag2 = 0
        for k in password:
            if k in dec_numbers:
                flag1 = 1
            if k in spec_chars:
                flag2 += 1
        if flag2 + flag1 == 2:
            break
        else:
            password = ""
    return password

def create_unreal_password():
    """Library = dec_number + low_english + spec_chars + upper_english
        size password = 16"""

    libraries = dec_numbers + spec_chars + upper_english + low_english
    password = ''
    while True:
        for i in range(16):  # size password
            password += random.choice(libraries)

        flag1 = 0
        flag2 = 0
        flag3 = 0
        for k in password:
            if k in dec_numbers:
                flag1 = 1
            if k in spec_chars:
                flag2 = 1
            if k in upper_english:
                flag3 = 1
        if flag1 + flag2 + flag3 == 3:
            break
        else:
            password = ""
    return password

def create_own_password(size, libraries_str):
    while True:
        password = ""
        libraries = ""
        if len(libraries_str) > 4:
            libraries = libraries_str
            for i in range(size):  # size password
                password += random.choice(libraries)
            return password

        else:
            for library in libraries_str:
                if library == '1':
                    libraries += dec_numbers
                elif library == '2':
                    libraries += low_english
                elif library == '3':
                    libraries += upper_english
                elif library == '4':
                    libraries += spec_chars
                else:
                    return "Error. You specified a non-existent library"

            for i in range(size):  # size password
                password += random.choice(libraries)

            flag1 = 0
            flag2 = 0
            flag3 = 0
            flag4 = 0
            for k in password:
                if k in dec_numbers:
                    flag1 = 1
                if k in spec_chars:
                    flag2 = 1
                if k in upper_english:
                    flag3 = 1
                if k in low_english:
                    flag4 = 1
            if flag1 + flag2 + flag3 + flag4 == len(libraries_str):
                break
            else:
                password = ""


    return password


