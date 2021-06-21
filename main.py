import sys
import time
decore1 = "==============================="
byetext = "\n\nThanks For Using Our Program\n\nExiting..."
print(decore1)
print("\nWelcome To PyCalc Project: CLI Edition\n")
print(decore1)
time.sleep(0.2)
print("\nVersion:4.2 Developers Preview\n")
print(decore1)
print("Copyright © 2021 TechVio")
time.sleep(0.5)
print(decore1)
print("The Project Link: https://www.github.com/techvio1/PyCalc-Project/")
print(decore1)
time.sleep(3)
print("Licensed Under MIT License: https://mit-license.org/")
print(decore1)
time.sleep(0.2)
print("running...")


def calculator():

    time.sleep(1.0)
    print(decore1)
    num1 = float(input("Enter Your First Number: "))
    print(decore1)
    time.sleep(0.1)
    operation = input("Enter Your Operation: ")
    print(decore1)
    time.sleep(0.1)
    num2 = float(input("Enter Your Second Number:"))
    print(decore1)
    time.sleep(0.1)
    if operation == "*":
        result = float(num1*num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calculator()
        else:
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
    elif operation == "+":
        result = float(num1+num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calculator()
        else:
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
    elif operation == "-":
        result = float(num1-num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calculator()
        else:
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
    elif operation == "/":
        result = float(num1/num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calculator()
        else:
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
    elif operation == "%":
        result = float(num1 % num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calculator()
        else:
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
    elif operation == "**":
        result = float(num1**num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calculator()
        else:
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
    elif operation == "//":
        result = float(num1//num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calculator()
        else:
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
    else:
        time.sleep(0.5)
        print("Error: Incorrect Operation:")
        time.sleep(0.5)
        print("=====================")
        print("Addition:         +")
        print("=====================")
        print("Subtraction:      -")
        print("=====================")
        print("Multiplication:   *")
        print("=====================")
        print("Division:         /")
        print("=====================")
        print("Modulus:          %")
        print("=====================")
        print("Exponentiation:   **")
        print("=====================")
        print("Floor division:   //")
        print("=====================")
        time.sleep(1.0)
        calculator()


calculator()
