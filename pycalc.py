import sys
decore = "--------------------------------------"
qtxt = "\n\nThank you For Using Our Program\nExiting..."
pccv = "V2.0 build 021922"
reqtxt = "Do you want to do another operation (y/n/q): "
btc = "\nBack to the console\n"
badparam = "\nIncorrect parameter, back to console\n"
print(decore+"\nWelcome to PyCalc project: CLI Edition\n"+decore+"\nVersion: 7.0\n"+"Branch: Stable\n"+decore+"\nCopyright © 2022 TechVio\n"+decore+"\nLicensed under MIT license\n"+decore+"\nPyCalc console "+pccv+"\n"+decore)


def calcreq():
    req = str.lower(input(reqtxt))
    match req:
        case 'y':
            calc()
        case 'n':
            print(decore + btc + decore)
            console()
        case 'q':
            print(qtxt)
            sys.exit()
        case _:
            print(decore + badparam + decore)
            console()


def mcalcreq():
    req = str.lower(input(reqtxt))
    match req:
        case 'y':
            mcalc()
        case 'n':
            print(decore+btc+decore)
            console()
        case 'q':
            print(qtxt)
            sys.exit()
        case _:
            print(decore+badparam+decore)
            console()


def sqrtreq():
    req = str.lower(input(reqtxt))
    match req:
        case 'y':
            sqrt()
        case 'n':
            print(decore + btc + decore)
            console()
        case 'q':
            print(qtxt)
            sys.exit()
        case _:
            print(decore + badparam + decore)
            console()


def calc():
    print(decore)
    n1 = float(input("Enter Your First Number: "))
    print(decore)
    op = input("Enter Your Operation: ")
    print(decore)
    n2 = float(input("Enter Your Second Number:"))
    print(decore)
    match op:
        case "*":
            result = float(n1*n2)
            print(result)
            calcreq()
        case "+":
            result = float(n1+n2)
            print(result)
            calcreq()
        case "-":
            result = float(n1-n2)
            print(result)
            calcreq()
        case "/":
            result = float(n1/n2)
            print(result)
            calcreq()
        case "%":
            result = float(n1 % n2)
            print(result)
            calcreq()
        case "**":
            result = float(n1**n2)
            print(result)
            calcreq()
        case "//":
            result = float(n1//n2)
            print(result)
            calcreq()
        case _:
            print("Error: Incorrect operation:"+"\nAddition      : +"+"\nSubtraction   : -"+"\nMultiplication: *"+"\nDivision      : /"+"\nModulus       : %"+"\nExponentiation: **"+"\nFloor division: //")
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
    calcul = input("Type calculation: ")
    print(str(eval(calcul)))
    print(decore)
    mcalcreq()


def console():
    calcmode = str.lower(input("Select Calculator Mode: "))
    match calcmode:
        case "help":
            print(decore+'\nNormal calculator mode             : "calc"'+'\nMulti-operations calculator mode: "mcalc"'+'\nsquare root mode                   : "sqrt"'+'\nConsole version                    : "version"'+'\nProject links                      : "projectlinks"\n'+decore)
            console()
        case "calc":
            calc()
        case "mcalc":
            mcalc()
        case "sqrt":
            sqrt()
        case "version":
            print(pccv)
            console()
        case "exit":
            print(qtxt)
            sys.exit()
        case "projectlinks":
            print("Github: https://www.github.com/techvio1/PyCalc-Project/"+"\nGitLab: Working on final touches")
            console()
        case _:
            print(decore+"\nIncorrect mode: Type 'help' for more informations\n"+decore)
            console()


console()
