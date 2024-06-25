import math, os, random, sys
import pyperclip
from termcolor import colored, cprint

os.system("cls" if os.name == "nt" else "clear")


def write_out(text, color="white", pad_top=1, pad_bottom=1):

    top = "".join(["\n" for i in range(pad_top)])
    bottom = "".join(["\n" for i in range(pad_bottom)])

    print(colored(top + text + bottom, color))


def choose_characters(password, characters_to_chose):

    for i in range(len(password)):
        if math.trunc(random.random() * 100) > 79:
            password[i] = random.choice(characters_to_chose)


def generate_password(password_length, use_upper, use_digits, use_special_chars):

    lower = [chr(i) for i in range(97, 97 + 26)]

    return_password = [random.choice(lower) for i in range(password_length)]

    if use_digits:
        digits = [chr(i) for i in range(48, 58)]
        choose_characters(return_password, digits)

    if use_special_chars:
        special_chars = [chr(i) for i in range(37, 48)]
        choose_characters(return_password, special_chars)

    if use_upper:
        upper = [chr(i) for i in range(65, 65 + 26)]
        choose_characters(return_password, upper)

    return "".join(return_password)


running = True

while running:
    write_out("-- Password Generator --", "yellow")
    print(colored("Choose option:", "light_blue"))
    print(colored("1: generate password", "light_blue"))
    print(colored("2: exit the program", "light_blue"))

    try:
        user_choice = int(input("\nYour choice: "))

        match (user_choice):
            case 1:
                password_length = 0

                while password_length < 5:
                    password_length = int(input("Provide password length: "))

                    if password_length < 5:
                        password_length = 0
                        write_out("Passwords must be at least 5 characters long", "red")

                use_upper = input("Use uppercase letters? (y/n) ") == "y"
                use_digits = input("Use digits? (y/n) ") == "y"
                use_special_chars = input("Use special characters? (y/n) ") == "y"

                password = generate_password(
                    password_length, use_upper, use_digits, use_special_chars
                )
                
                print("Generated Password: ", end="")
                write_out(password, "light_green")

                pyperclip.copy(password)
                print("Copied password to clipboard!\n")
            case 2:
                write_out("Bye!", "yellow")
                running = False
            case _:
                raise ValueError

    except ValueError:
        write_out("Please enter a correct value!", "red")
