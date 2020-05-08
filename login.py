users = {}
status = ""

def displayMenu():
    status = input("Are you a returning user? (y/n) Press q to quit\n")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    else:
        print ("Please enter 'y' or 'n'.")

def newUser():
    createLogin = input("Create a username: ")

    if createLogin in users:
        print("\nLogin name already exists. Please enter a new one.\n")
    else:
        createPassw=input("Create a password: ")
        users[createLogin]=createPassw
        print ("\nUser created.\n")

def oldUser():
    login = input("Enter your login: ")
    passw = input("Enter your password: ")

    if login in users and passw==users[login]:
        print ("Success.")
    else:
        print ("Please try again.")

while status !="q":
    displayMenu()
