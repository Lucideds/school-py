import random
say = ["Simon says... ", ""]
simon_says = ["Hands on head", "Hands on ears", "Right hand up", "Left hand up", "Hands on shoulders"]
index = random.randint(0,4)
instruction = simon_says[index]
index = random.randint(0,1)
does_say = say[index]
print(f"{does_say}{instruction}") 
