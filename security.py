import time
from users_login_info import *


def usr(real_user):
    usr = input("Enter username: ")
    if usr == real_user:
        time.sleep(1)
        print("Done")
    elif usr != real_user:
        time.sleep(1)
        print("Username not found!")
        exit()


def pwd(real_pwd):
    pwd = input("Enter password: ")
    if pwd == real_pwd:
        time.sleep(1)
        print("Login successfully!")
    elif pwd != real_pwd:
        time.sleep(1)
        print("Incorrect password!")


def secure(real_user, real_pwd):
    usr(real_user)
    pwd(real_pwd)


def add_to_database(username, password):
    pick(username, password)
    with open("users_login_info.py", "a+") as write:
        write.write(f"""users = {users}
passwords = {passwords}

def pick(username, password):
    users.append(username)
    passwords.append(password)""")


def sign_up():
    if len(users) == len(passwords):
        username_input = input("Pick a username: ")
        if username_input == "":
            print("Your username is empty!")
            sign_up()
        if username_input not in users:
            password_input = input("Enter your password: ")
            retype_password = input("Re-enter your password: ")
            if password_input == retype_password:
                add_to_database(username_input, password_input)
                print("Your account have been done successfully. You can go and log in from your account")
            else:
                print("The passwords you typed doesn't matches!")
                print("Sorry you should retry your sign up!")
                sign_up()
        elif username_input in users:
            print("Sorry, this username is already taken!")
            print("Retry to sign up!")
            sign_up()
    elif len(users) != len(passwords):
        print("There's an error in the database, try again later!")


def login(signup=True):
    username_input = input("Enter your username: ")
    for i in range(len(users)):
        if username_input == users[i]:
            password_input = input("Enter your password: ")
            if password_input == passwords[i]:
                print(f"You have been successfully loged in.")
            else:
                print("Wrong password!")
                exit()
    if username_input not in users:
        print("No such username in our database!")
        if signup == True:
            choice = input("Would you like to sign up? (Y/N) ").lower()
            if choice == "y" or choice == "yes":
                sign_up()
        else:
            exit()

