import sys
import time

decore = "==============================="
byetext = "\n\nThank you For Using Our Program\n\nExiting..."
print(decore)
print("\nWelcome To PyCalc Project: CLI Edition\n")
print(decore)
time.sleep(0.2)
print("\nVersion:5.1\n")
print("Branch: Stable")
print(decore)
print("Copyright © 2021 TechVio")
time.sleep(0.5)
print(decore)
print("Project Link: https://www.github.com/techvio1/PyCalc-Project/")
print(decore)
time.sleep(1)
print("License: MIT License: https://mit-license.org/")
print(decore)
time.sleep(0.2)
print("running...")


def calc():
    time.sleep(1.0)
    print(decore)
    num1 = float(input("Enter Your First Number: "))
    print(decore)
    time.sleep(0.1)
    operation = input("Enter Your Operation: ")
    print(decore)
    time.sleep(0.1)
    num2 = float(input("Enter Your Second Number:"))
    print(decore)
    time.sleep(0.1)
    if operation == "*":
        result = float(num1 * num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n/q): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calc()
        elif request == 'n':
            print("Back To Console")
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print("Incorrect Parameter, back to console")
            time.sleep(1.5)
            console()
    elif operation == "+":
        result = float(num1 + num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n/q): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calc()
        elif request == 'n':
            print("Back To Console")
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print("Incorrect Parameter, back to console")
            time.sleep(1.5)
            console()
    elif operation == "-":
        result = float(num1 - num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n/q): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calc()
        elif request == 'n':
            print("Back To Console")
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print("Incorrect Parameter, back to console")
            time.sleep(1.5)
            console()
    elif operation == "/":
        result = float(num1 / num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n/q): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calc()
        elif request == 'n':
            print("Back To Console")
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print("Incorrect Parameter, back to console")
            time.sleep(1.5)
            console()
    elif operation == "%":
        result = float(num1 % num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n/q): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calc()
        elif request == 'n':
            print("Back To Console")
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print("Incorrect Parameter, back to console")
            time.sleep(1.5)
            console()
    elif operation == "**":
        result = float(num1 ** num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n/q): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calc()
        elif request == 'n':
            print("Back To Console")
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print("Incorrect Parameter, back to console")
            time.sleep(1.5)
            console()
    elif operation == "//":
        result = float(num1 // num2)
        print(result)
        time.sleep(0.5)
        request = input("Do you want to do another operation (y/n/q): ")
        if request == "y":
            print("Please Wait...")
            time.sleep(1.0)
            calc()
        elif request == 'n':
            print("Back To Console")
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print("Incorrect Parameter, back to console")
            time.sleep(1.5)
            console()
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
        calc()


def squareroot():
    from math import sqrt
    num = float(input("Enter A Number: "))
    result = sqrt(num)
    print(result)
    request = input("Do you want to do another square root operation ? (y/n/q): ")
    if request == 'y':
        squareroot()
    elif request == 'n':
        console()
    elif request == 'q':
        time.sleep(0.5)
        print(byetext)
        time.sleep(0.5)
        sys.exit()
    else:
        print("Incorrect Parameter, back to console")
        time.sleep(1.5)
        console()


def console():
    calculator_mode = input("Select Calculator Mode: ")
    if calculator_mode == "help":
        print(decore)
        print('square root mode: "sqrt"')
        print('normal Calculator Mode: "calc"')
        print('console version: "version"')
        print(decore)
        console()
    elif calculator_mode == "calc":
        calc()
    elif calculator_mode == "sqrt":
        squareroot()
    elif calculator_mode == "version":
        print("pycalc console v1.0 build 062621")
        console()
    elif calculator_mode == "exit":
        time.sleep(0.5)
        print(byetext)
        time.sleep(0.5)
        sys.exit()
    else:
        print(decore)
        print("Incorrect mode: Type 'help' for more information")
        print(decore)
        console()


console()
