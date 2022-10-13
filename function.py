import generator

def hello():
    """Welcome menu."""
    print("Hello. I am a generator password. And I can create a new password for you!")

def what_your_type_password():
    """Letter for user about choice_type_password"""
    print("Now you can choice type of password. If you don't know types of password that write command /wtp.")

def about_types_of_password():
    """All about types of password in generator!"""

    return """
Types of password:
    
    1) Standard password (size=8, libraries = low_english + dec_numbers
    2) Password for phone (size=6, library = dec_numbers)
    3) Difficult password (size=12, libraries = low_english + dec_numbers + spec_chars)
    4) Unreal password (size=16, libraries = low_english + dec_numbers + spec_chars + upper_english)
    5) Own password (size=1-50, libraries = any, other conditions)"""

def choice_type_password(n):
    """Here user choices type of password

    int(n) -> type_of_password

    About types of password you can write in README or in command /wtp"""

    if n == 1:
        return generator.create_standart_password()
    elif n == 2:
        return generator.create_password_phone()
    elif n == 3:
        return generator.create_difficult_password()
    elif n == 4:
        return generator.create_unreal_password()
