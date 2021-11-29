import sys
decore = "-------------------------------"
byetext = "\n\nThank you For Using Our Program\n\nExiting..."
print(decore)
print("\nWelcome To PyCalc Project: CLI Edition\n")
print(decore)
print("\nVersion:6.0\n")
print("Branch: Unstable")
print(decore)
print("Copyright © 2021-2022 TechVio")
print(decore)
print("Licensed under MIT License: https://mit-license.org/")
print(decore)
print("Starting The Console...")
print(decore)


def calcreq():
    request = input("Do you want to do another operation (y/n/q): ")
    if request == "y":
        print("Please Wait...")
        calc()
    elif request == 'n':
        print(decore)
        print("Back To Console")
        print(decore)
        console()
    elif request == 'q':
        print(byetext)
        sys.exit()
    else:
        print(decore)
        print("Incorrect Parameter, back to console")
        print(decore)
        console()


def mcalcreq():
    request = input("Do you want to do another operation (y/n/q): ")
    if request == "y":
        print("Please Wait...")
        mcalc()
    elif request == 'n':
        print(decore)
        print("Back to console")
        print(decore)
        console()
    elif request == 'q':
        print(byetext)
        sys.exit()
    else:
        print(decore)
        print("Incorrect parameter, back to console")
        print(decore)
        console()


def sqrtreq():
    request = input("Do you want to do another operation (y/n/q): ")
    if request == "y":
        print("Please Wait...")
        sqrt()
    elif request == 'n':
        print(decore)
        print("Back to console")
        print(decore)
        console()
    elif request == 'q':
        print(byetext)
        sys.exit()
    else:
        print(decore)
        print("Incorrect parameter, back to console")
        print(decore)
        console()


def calc():

    print(decore)
    num1 = float(input("Enter Your First Number: "))
    print(decore)
    operation = input("Enter Your Operation: ")
    print(decore)
    num2 = float(input("Enter Your Second Number:"))
    print(decore)
    if operation == "*":
        result = float(num1 * num2)
        print(result)
        calcreq()
    elif operation == "+":
        result = float(num1 + num2)
        print(result)
        calcreq()
    elif operation == "-":
        result = float(num1 - num2)
        print(result)
        calcreq()
    elif operation == "/":
        result = float(num1 / num2)
        print(result)
        calcreq()
    elif operation == "%":
        result = float(num1 % num2)
        print(result)
        calcreq()
    elif operation == "**":
        result = float(num1 ** num2)
        print(result)
        calcreq()
    elif operation == "//":
        result = float(num1 // num2)
        print(result)
        calcreq()
    else:
        print(decore)
        print("Error: Incorrect Operation:")
        print(decore)
        print(decore)
        print("Addition      : +")
        print(decore)
        print("Subtraction   : -")
        print(decore)
        print("Multiplication: *")
        print(decore)
        print("Division      : /")
        print(decore)
        print("Modulus       : %")
        print(decore)
        print("Exponentiation: **")
        print(decore)
        print("Floor division: //")
        print(decore)
        calc()


def sqrt():
    from math import sqrt as sqrtmath
    print(decore)
    num = float(input("Enter A Number: "))
    print(decore)
    result = sqrtmath(num)
    print(result)
    print(decore)
    sqrtreq()


def mcalc():
    calc = input("Type calculation: ")
    print(str(eval(calc)))
    print(decore)
    mcalcreq()


def console():
    calcmode = input("Select Calculator Mode: ")
    if calcmode == "help":
        print(decore)
        print('normal Calculator Mode             : "calc"')
        print('Multiple operations calculator mode: "mcalc"')
        print('square root mode                   : "sqrt"')
        print('console version                    : "version"')
        print('Project Links                      : "projectlinks"')
        print(decore)
        console()
    elif calcmode == "calc":
        calc()
    elif calcmode == "sqrt":
        sqrt()
    elif calcmode == "version":
        print("pycalc console v1.3 build 112821")
        console()
    elif calcmode == "exit":
        print(byetext)
        sys.exit()
    elif calcmode == "projectlinks":
        print("Github: https://www.github.com/techvio1/PyCalc-Project/")
        print("GitLab: not ready yet")
        console()
    elif calcmode == "mcalc":
        mcalc()
    else:
        print(decore)
        print("Incorrect mode: Type 'help' for more information")
        print(decore)
        console()


console()
