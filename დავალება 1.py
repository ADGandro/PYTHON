import random


a = random.randint(1, 100)
b = random.randint(1, 100)

print("a:", a)
print("b:", b)

if a % 2 == 0 and b % 2 == 0:
    result = a ** b
    print("a ** b =", result)


elif a % 2 == 0 and b % 2 != 0:
    result = a * b
    print("a * b =", result) 

elif a % 2 != 0 and b % 2 != 0:
    c = random.randint(1, 100)
    print("c", c)
    result = a * b * c
    print("a * b * c =", result)
