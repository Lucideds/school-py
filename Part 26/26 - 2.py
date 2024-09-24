file = open("txt/calculation.txt", "w")

print("Would you like to 1. add, 2. divide, 3. multiply or 4. subtract? Enter 1 to 4")
choice = int(input())
number1 = int(input("Enter your first number: "))
number2 = int(input("Enter your second number: "))

def calc(a, num1, num2):
    if a == 1:
        ans = num1 + num2
    elif a == 2:
        ans = num1 / num2
    elif a == 3:
        ans = num1 * num2
    elif a == 4:
        ans = num1 - num2
    return ans
answer = calc(choice, number1, number2)
file.write(str(answer))
file.close()
