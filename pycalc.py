import sys
import time

decore = "-------------------------------"
byetext = "\n\nThank you For Using Our Program\n\nExiting..."
print(decore)
print("\nWelcome To PyCalc Project: CLI Edition\n")
print(decore)
time.sleep(0.2)
print("\nVersion:6.0\n")
print("Branch: Unstable")
print(decore)
print("Copyright © 2021-2022 TechVio")
time.sleep(0.5)
print(decore)
print("Licensed under MIT License: https://mit-license.org/")
print(decore)
time.sleep(0.2)
print("Starting The Console...")
print(decore)
time.sleep(1)

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
            print(decore)
            print("Back To Console")
            print(decore)
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
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
            print(decore)
            print("Back To Console")
            print(decore)
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
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
            print(decore)
            print("Back To Console")
            print(decore)
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
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
            print(decore)
            print("Back To Console")
            print(decore)
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
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
            print(decore)
            print("Back To Console")
            print(decore)
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
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
            print(decore)
            print("Back To Console")
            print(decore)
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
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
            print(decore)
            print("Back To Console")
            print(decore)
            time.sleep(1)
            console()
        elif request == 'q':
            time.sleep(0.5)
            print(byetext)
            time.sleep(0.5)
            sys.exit()
        else:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
            time.sleep(1.5)
            console()
    else:
        time.sleep(0.5)
        print(decore)
        print("Error: Incorrect Operation:")
        print(decore)
        time.sleep(0.5)
        print("=====================")
        print("Addition       :   +")
        print("=====================")
        print("Subtraction    :   -")
        print("=====================")
        print("Multiplication :   *")
        print("=====================")
        print("Division       :   /")
        print("=====================")
        print("Modulus        :   %")
        print("=====================")
        print("Exponentiation :   **")
        print("=====================")
        print("Floor division :   //")
        print("=====================")
        time.sleep(1.0)
        calc()


def squareroot():
    from math import sqrt
    print(decore)
    num = float(input("Enter A Number: "))
    print(decore)
    result = sqrt(num)
    print(result)
    print(decore)
    request = input("Do you want to do another square root operation ? (y/n/q): ")
    if request == 'y':
        squareroot()
    elif request == 'n':
        print(decore)
        print("Back to console")
        print(decore)
        console()
    elif request == 'q':
        time.sleep(0.5)
        print(byetext)
        time.sleep(0.5)
        sys.exit()
    else:
        print(decore)
        print("Incorrect Parameter, back to console")
        print(decore)
        time.sleep(1.5)
        console()
#def testing():
#    calc = input("Type calculation: ")
#
#    print("Answer: " + str(eval(calc)))
#testing()

def console():
    calculator_mode = input("Select Calculator Mode: ")
    if calculator_mode == "help":
        print(decore)
        print('square root mode      : "sqrt"        ')
        print('normal Calculator Mode: "calc"        ')
        print('eval mode:            : "eval"        ')
        print('console version       : "version"     ')
        print('Project Links         : "projectlinks"')
        print(decore)
        console()
    elif calculator_mode == "calc":
        calc()
    elif calculator_mode == "sqrt":
        squareroot()
    elif calculator_mode == "version":
        print("pycalc console v1.2 build 080221")
        console()
    elif calculator_mode == "exit":
        time.sleep(0.5)
        print(byetext)
        time.sleep(0.5)
        sys.exit()
    elif calculator_mode == "projectlinks":
        print("Github: https://www.github.com/techvio1/PyCalc-Project/")
        print("GitLab: Working on it")
        console()

    else:
        print(decore)
        print("Incorrect mode: Type 'help' for more information")
        print(decore)
        console()


console()