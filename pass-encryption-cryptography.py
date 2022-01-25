# Ask the user if want to add/view credentials
# Encrypt password each time user adds credentials & decrypt password each time user wants to view

from cryptography.fernet import Fernet

mode = input("Do you want to add/view credentals (view)/ (add)? , enter q to quit: ").lower()

'''
# Use onece to generate & save key then comment out

def write_key():
    key = Fernet.generate_key()
    with open("keyfile.key", "wb") as k:
        k.write(key)
    return key'''

# Get key
def read_key():
    with open("keyfile.key", "rb") as k:
        key = k.read()
    return key

fer = Fernet(read_key())

if mode == "add":
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("credentials.txt", "a") as f:
        f.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n")
elif mode == "view":
    with open("credentials.txt", "r") as f:
        for line in f.readlines():
            #username, password = line.split("|")
            username = line.split("|")[0]
            password = line.split("|")[1]
            print("Username: ", username, "\nPassword: ", fer.decrypt(password.encode()).decode())
elif mode == "q":
    quit()
else:
    print("Enter a valid option next time.")