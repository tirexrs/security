# security
This is a python module that helps you add a simple security to your python projects.
To add a security to project, you should first downloading the security.py file and put it in the same path with your project file, or with the modules path.
Then, if you need to create a simple security (you choose the username and the password, and the user should know them before accessing your project), between your code and the "import security" line, write on a new single line: "securirty.secure("username", "password"), with the username and the password of your choice.
If you need to create a login and signup for your script, insteed writing "security.secure("username", "password"), write security.login()
You can pass True or False, inside the "security.login()", and if you pass False, the user won't be able to sign up if he doesn't already have a username and a password.
If you don't pass anything, by default it's value is True.
Usernames and passwords when you sign up will be saved in users_login_info.py, so the script can access them when you need to login.
