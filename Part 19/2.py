shopping = []
while True:
    ans = input("Would you like to edit your shopping list? Y/N: ")
    if ans.lower() == "y":
        ans = input("Would you like to add or remove an item? A/R: ")
        if ans.lower() == "a":
            item = input("Enter an item to add: ")
            shopping.append(item)
        elif ans.lower() == "r":
            item = input("Enter an item to remove: ")
            shopping.remove(item)       
    else:
        print(shopping)
        break
    
