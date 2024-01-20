def mult(x, y):
    """Returns x multiplied by y"""
    return x * y


def add(x, y):
    """Returns x add y"""
    return x + y


def minus(x, y):
    """Returns x minus y"""
    return x - y


def div(x, y):
    """Returns x divided by y"""
    return x / y


def getnumberinputS(
    prompt,
):  # S for strict (does not allow any other input, only int or float)
    while True:
        num = input(prompt)
        try:
            val = float(num)
            return val
        except ValueError:
            try:
                val = int(num)
                return val
            except ValueError:
                print("Invalid input, please enter Float or Int")



def getnumberinputL(
    prompt,
):  # L for lenient (allows anything else and returns "" if not int/float)
    while True:
        num = input(prompt)
        try:
            val = int(num)
            return val
        except ValueError:
            try:
                val = float(num)
                return val
            except ValueError:
                return ""


def Eqsolve(aName, bName, cName, aUnits, bUnits, cUnits, Eqf):
    """Welcome to Equation Solver, Please press enter on an unknown value to solve for it, enter the other two values in the requested format and it will handle the rest!"""
    eqf = Eqf.split(
        "."
    )  # split the three terms and the operator in eqf[0:2] and operator in eqf[3]
    equation = f"{eqf[0]} = {eqf[1]} {eqf[3]} {eqf[2]}"  # eqf[3] is the operator when the formula has not been rearranged
    print(Eqsolve.__doc__)  # prints docstring as an intro on how to use
    print(f"{equation} is the formula being used ")
    a = getnumberinputL(
        f"Please enter {aName} in {aUnits}: "
    )  # getting float or int input
    if a == "":
        a = 0
    b = getnumberinputL(f"Please enter {bName} in {bUnits}: ")
    if b == "":
        b = 0
    c = getnumberinputL(f"Please enter {cName} in {cUnits}: ")
    if c == "":
        c = 0
    if a == 0:
        print(f"{aName} is the unknown")  # printing the unknown name
        if eqf[3] == "/":
            ans = div(b, c)  # normal operator (No rearrange required)
        elif eqf[3] == "*":
            ans = mult(b, c)  # normal operator
        elif eqf[3] == "+":
            ans = add(b, c)  # normal operator
        return aName, ans, aUnits  # returns Name, Value and Units
    if b == 0:
        print(f"{bName} is the unknown")
        if eqf[3] == "/":
            ans = mult(a, c)  # rearranged operator
        elif eqf[3] == "*":
            ans = div(a, c)  # rearranged operator
        elif eqf[3] == "+":
            ans = minus(a, c)  # rearranged operator
        return bName, ans, bUnits  # returns Name, Value and Units
    if c == 0:
        print(f"{cName} is the unknown")
        if eqf[3] == "/":
            ans = div(a, b)  # rearranged operator
        elif eqf[3] == "*":
            ans = div(a, c)  # rearranged operator
        elif eqf[3] == "+":
            ans = minus(a, c)  # rearranged operator
        return bName, ans, cUnits  # returns Name, Value and Units


if __name__ == "__main__":
    Eqsolve("Speed", "Distance", "Time", "m/s", "m", "s", "S.D.T./")
