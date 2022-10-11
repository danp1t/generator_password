#Python libraries
import random

#libraries for generator (CONST)
low_english = "zxcvbnmasdfghjklpoiuytrewq"
dec_numbers = '0123456789'


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
