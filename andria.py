def login(username, password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    if username == "kobe2bbryant123456789@gmail.com" and password == "Andrikuz":
        return "Login successful!"
    elif username == "static_username":
        return "Incorrect password. Try again."
    elif password == "static_password":
        return "Incorrect username. Try again."
    else:
        return "Tinky Winky"

username = input("Enter username: ")
password = input("Enter password: ")

print(login(username, password))