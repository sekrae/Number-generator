import random


#This is a simple code that returns a random number from low num to high num!


print("THis program intakes two numbers and randomly generates a number between them.")
low = int(input("What is lower number in your range? "))
high = int(input("What is higher number in your range? "))
num = random.randint(low, high)
print(f"Your number is {num}")
