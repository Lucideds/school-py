passwords = [[],
             [],
             []] 
passwords[0].append("RasberryPiOS")
passwords[1].append("pi")
passwords[2].append("rasberry")

loop = True
while loop:
    print("The current password 'database' is:")
    print(passwords)
    x = input("Do you want to enter a new password? Y/N : ")
    if x.lower() == "y":
        password_confirm = ""
        account = input("Please enter a account name: ")
        passwords[0].append(account)
        username = input("Please enter a username: ")
        passwords[1].append(username)
        password = input("Please enter a password (Case Sensitive): ")
        passwords[2].append(password)
        while password != password_confirm:
            password_confirm = input("Please repeat the password (Case Sensitive): ")
    else:
        print("Exiting...")
        loop = False
print("The 'database' is:")
print(passwords)

        
