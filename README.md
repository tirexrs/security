# security
This is a python module that helps you add a simple security to your python projects.
To add a login to your project, you should first download the security.py file and copy it to the same path of your project's file, or with the modules path.
You have to import the security file (module), to your project.
Then, if you need to create a simple login (you choose the username and the password, and the user should know them before accessing your project), between your code and the "import security" line, write on a new single line: "securirty.secure("username", "password"), with the username and the password of your choice.
If you need to create a login and signup for your script, insteed writing "security.secure("username", "password"), write security.login()
You can pass True or False, inside the "security.login()", and if you pass False, the user won't be able to sign up if he doesn't already have a username and a password.
If you don't pass anything, by default it's value is True.
Usernames and passwords when you sign up will be saved in users_login_info.py, so the script can access them when you need to login.
A new feature for this module is now avilable, you can import this module into any blank python script, and after importing, use "security.encrypt_script()", and this will ask you to choose the python file you want to encrypted, and any name to create a new file for the encrypted script.
So with "security.encrypt_script()", the script will work fine, but you cannot understand what's inside the code, and it can't be reverse engineered (only if the script is re-decrypted).
