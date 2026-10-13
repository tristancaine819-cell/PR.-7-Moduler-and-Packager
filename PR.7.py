import datetime
import math
import random
import csv
import os

print("================================")
print(" Welcome to Python Project")
print("================================")

while True:
    print("\nMAIN MENU")
    print("1. Date and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Module")
    print("4. File Operations")
    print("5. Explore Module Attributes")
    print("6. Exit")

    choice = input("Enter your choice: ")

    # DATE AND TIME
    if choice == "1":
        print("\nDate and Time Operations")
        print("1. Display current date and time")
        print("2. Calculate difference between dates")
        print("3. Format date")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            now = datetime.datetime.now()
            print("Current date and time:", now)

        elif ch == "2":
            date1 = input("Enter first date (YYYY-MM-DD): ")
            date2 = input("Enter second date (YYYY-MM-DD): ")

            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

            difference = abs((d2 - d1).days)
            print("Difference is", difference, "days")

        elif ch == "3":
            today = datetime.datetime.now()
            print("Formatted Date:", today.strftime("%d-%m-%Y"))
            print("Date and Month: ", today.strftime("%A,%B"))

        elif ch == "4":
                stamp = datetime.datetime.now().timestamp()
                print("Current timestamp: ", stamp)
                print("COverted Data: ", datetime.datetime.fromtimestamp(stamp))

        elif ch == "5":
            date1 = input("Enter first date(YYYY-MM-DD): ")
            date2 = input("Enter Second Date(YYYY-MM-DD): ")

        elif ch == "6":
            break

        else:
            print("Invalid choice")

    # MATHEMATICAL OPERATIONS
    elif choice == "2":
        print("\nMathematical Operations")
        print("1. Basic Calculator")
        print("2. Factorial")
        print("3. Square Root")
        print("4. Power")
        print("5. Area of Circle")
        print("6. Back to main menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")

            op = input("Enter operation: ")

            if op == "1":
                print("Answer:", a + b)
            elif op == "2":
                print("Answer:", a - b)
            elif op == "3":
                print("Answer:", a * b)
            elif op == "4":
                if b != 0:
                    print("Answer:", a / b)
                else:
                    print("Cannot divide by zero")
            else:
                print("Invalid operation")

        elif ch == "2":
            n = int(input("Enter a number: "))
            if n >= 0:
                print("Factorial:", math.factorial(n))
            else:
                print("Enter a positive number")

        elif ch == "3":
            n = float(input("Enter a number: "))
            if n >= 0:
                print("Square root:", math.sqrt(n))
            else:
                print("Enter a non-negative number")

        elif ch == "4":
            a = float(input("Enter base: "))
            b = float(input("Enter power: "))
            print("Answer:", math.pow(a, b))

        elif ch == "5":
            r = float(input("Enter radius: "))
            print("Area:", math.pi * r * r)

        elif ch == "6":
            break

        else:
            print("Invalid choice")

    #GENERATE UNIQUE IDENTIFICATION(UUID)
      elif choice == "4":
        print("\nUNIQUE IDENTIFIER")
        print("Generate UUID: ", uuid.uuid4())

    # RANDOM MODULE
    elif choice == "3":
        print("\nRandom Module")
        print("1. Random Number")
        print("2. Roll a Dice")
        print("3. Random Choice")
        print("4. Shuffle a list")
        print("5. Back to main menu")

        ch = input("Enter your choice: ")

        if ch == "1":
            a = int(input("Enter starting number: "))
            b = int(input("Enter ending number: "))
            print("Random number:", random.randint(a, b))

        elif ch == "2":
            print("Dice result:", random.randint(1, 6))

        elif ch == "3":
            fruits = ["Apple", "Mango", "Banana", "Orange"]
            print("Random fruit:", random.choice(fruits))

        elif ch == "4":
            items = input("Enter Items seperated by commas: ").split(" , ")
            random.shuffle(items)
            print("Shuffled list: ", items)

        elif ch == "5":
            break

        else:
            print("Invalid choice")

    # FILE OPERATIONS
    elif choice == "4":
        print("\nFile Operations")
        print("1. Create and Write File")
        print("2. Write to a File")
        print("3. Read from a File")
        print("4. Append to a File")
        print("5. Search in a File")
        print("6. Delete a File")

        ch = input("Enter your choice: ")
        name = input("Enter file name: ")

        if ch == "1":
            with open(name, "w") as f:
                text = input("Enter text: ")
                f.write(text)
            print("File created successfully")

        elif ch == "2":
            with open(name, "w") as f:
                text = input("Enter text: ")
                f.write(text)
            print("File written successfully")

        elif ch == "3":
            if os.path.exists(name):
                with open(name, "r") as f:
                    print(f.read())
            else:
                print("File not found")

        elif ch == "4":
            with open(name, "a") as f:
                text = input("Enter text: ")
                f.write("\n" + text)
            print("Text added successfully")

        elif ch == "5":
            if os.path.exists(name):
                word = input("Enter word to search: ")
                with open(name, "r") as f:
                    data = f.read()

                if word in data:
                    print("Word found")
                else:
                    print("Word not found")
            else:
                print("File not found")

        elif ch == "6":
            if os.path.exists(name):
                confirm = input("Delete this file? (yes/no): ")
                if confirm.lower() == "yes":
                    os.remove(name)
                    print("File deleted")
                else:
                    print("File not deleted")
            else:
                print("File not found")

        else:
            print("Invalid choice")

    # EXPLORE MODULES
    elif choice == "5":
        print("\nExplore Module Attributes")
        print("1. Math")
        print("2. Random")
        print("3. Date and Time")

        ch = input("Enter your choice: ")

        if ch == "1":
            print(dir(math))
        elif ch == "2":
            print(dir(random))
        elif ch == "3":
            print(dir(datetime))
        else:
            print("Invalid choice")
    
    #EXPLORE MODULE ATTRIBUTES
    elif choice == "8":
        print("!. Math Module")
        print("2. Random Module")
        print("3. Date and Time Module")

    ch = input("Enter your choice: ")

    if ch == "1":
     print(dir(math))
    elif ch == "2":
        print(dir(random))
    elif ch == "3":
        print(dir(datetime))

else:
    print("Invalid Choice.")


    # EXIT
    elif choice == "6":
        print("Thank you for using this project!")
        break

    else:
        print("Invalid choice. Try again.")