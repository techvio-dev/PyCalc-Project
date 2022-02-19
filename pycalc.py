import sys
decore = "--------------------------------------"
byetext = "\n\nThank you For Using Our Program\n\nExiting..."
print(decore + "\nWelcome to PyCalc project: CLI Edition\n" + decore)
print("Version: 7.0\n" + "Branch : Unstable pre-release\n" + decore)
print("Copyright © 2022 TechVio\n" + decore + "\nLicensed under MIT license\n" + decore)
print("Starting PyCalc console...\n" + decore)


def calcreq():
    req = str.lower(input("Do you want to do another operation (y/n/q): "))
    match req:
        case "y":
            print("please wait...")
            calc()
        case "n":
            print(decore + "\nBack to console\n" + decore)
            console()
        case "q":
            print(byetext)
            sys.exit()
        case _:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
            console()


def mcalcreq():
    req = str.lower(input("Do you want to do another operation (y/n/q): "))
    match req:
        case "y":
            print("please wait...")
            mcalc()
        case "n":
            print(decore + "\nBack to console\n" + decore)
            console()
        case "q":
            print(byetext)
            sys.exit()
        case _:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
            console()


def sqrtreq():
    req = str.lower(input("Do you want to do another operation (y/n/q): "))
    match req:
        case "y":
            print("please wait...")
            sqrt()
        case "n":
            print(decore + "\nBack to console\n" + decore)
            console()
        case "q":
            print(byetext)
            sys.exit()
        case _:
            print(decore)
            print("Incorrect Parameter, back to console")
            print(decore)
            console()


def calc():

    print(decore)
    num1 = float(input("Enter Your First Number: "))
    print(decore)
    op = input("Enter Your Operation: ")
    print(decore)
    num2 = float(input("Enter Your Second Number:"))
    print(decore)
    match op:
        case "*":
            result = float(num1 * num2)
            print(result)
            calcreq()
        case "+":
            result = float(num1 + num2)
            print(result)
            calcreq()
        case "-":
            result = float(num1 - num2)
            print(result)
            calcreq()
        case "/":
            result = float(num1 / num2)
            print(result)
            calcreq()
        case "%":
            result = float(num1 % num2)
            print(result)
            calcreq()
        case "**":
            result = float(num1 ** num2)
            print(result)
            calcreq()
        case "//":
            result = float(num1 // num2)
            print(result)
            calcreq()
        case _:
            print("Error: Incorrect Operation:")
            print("Addition      : +")
            print("Subtraction   : -")
            print("Multiplication: *")
            print("Division      : /")
            print("Modulus       : %")
            print("Exponentiation: **")
            print("Floor division: //")
            calc()


def sqrt():
    from math import sqrt
    print(decore)
    num = float(input("Enter A Number: "))
    print(decore)
    result = sqrt(num)
    print(result)
    print(decore)
    sqrtreq()


def mcalc():
    calc = input("Type calculation: ")
    print(str(eval(calc)))
    print(decore)
    mcalcreq()


def console():
    calcmode = str.lower(input("Select Calculator Mode: "))
    match calcmode:
        case "help":
            print(decore)
            print('normal Calculator Mode             : "calc"')
            print('Multiple operations calculator mode: "mcalc"')
            print('square root mode                   : "sqrt"')
            print('console version                    : "version"')
            print('Project Links                      : "projectlinks"')
            print(decore)
            console()
        case "calc":
            calc()
        case "mcalc":
            mcalc()
        case "sqrt":
            sqrt()
        case "version":
            print("pycalc console v2.0 build 021922")
            console()
        case "exit":
            print(byetext)
            sys.exit()
        case "projectlinks":
            print("Github: https://www.github.com/techvio1/PyCalc-Project/")
            print("GitLab: Working on final touches")
            console()
        case _:
            print(decore)
            print("Incorrect mode: Type 'help' for more information")
            print(decore)
            console()


console()
