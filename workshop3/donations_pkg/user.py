def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f"Welcome, {username}!")
            return username
        else:
            print("Invalid password.")
    else:
        print("Username not found.")
        return ""


def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print(f"Welcome, {username}! You are registered!!")
        return username
