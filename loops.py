# Loops
def usingFor():
    """Takes input and prints multiplication table of that number using while loop"""
    num = int(input("Enter a number: "))
    for i in range(1, 11):
        print(num, "X", i, "=", num*i)

def usingWhile():
    """Takes input and prints multiplication table of that number using while loop"""
    num = int(input("Enter a number: "))
    i = 1
    while i <= 10:
        print(num, "X", i, "=", num*i)
        i += 1

def reciprocal():
    """Takes input and prints reciprocal of that number using while loop"""
    num = int(input("Enter a number: "))
    i = 1
    while i <= num:
        print("1/", i, "=", 1/i)
        i += 1

def print_fruits():
    """Prints fruits using for loop"""
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            continue
        print(x)