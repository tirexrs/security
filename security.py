import time
from users_login_info import *
from getpass import getpass
from base64 import b64encode


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
        write.write("users = {users}\npasswords = {passwords}\n\ndef pick(username, password):\n    users.append(username)\n    passwords.append(password)")


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
                print("You have been successfully logged in.")
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


def encrypt_script():
    def read_file(file):
        with open(file, "r") as read:
            file_content = read.read()
        return file_content

    def check_filename(filename):
        if (str(filename[::-1])[:3])[::-1] != ".py":
            filename += ".py"
        return filename

    def get_file_info():
        print("Welcome to this project. You can here encrypt any python script in seconds!")
        file_input = input("Please enter the python file name: ")
        file = check_filename(file_input)
        try:
            read = read_file(file)
        except:
            print("Make to sure to enter the PATH of the file here, or copy the file to the same directory of this script!")
            exit()
        return read

    def encrypt_code():
        file_content = get_file_info()
        encrypted_file_name = input("Type a file name, to save the encrypted code in: ")
        encrypted_file_name = check_filename(encrypted_file_name)
        hidden_code = b64encode(file_content.encode())
        with open(encrypted_file_name, "w+") as write:
            write.write("from base64 import b64decode\n\ndef show(encrypted):\n    return b64decode(encrypted).decode()\nhidden = {hidden_code}\neval(compile(show(hidden), '<string>', 'exec'))")

    encrypt_code()
