def mult(a, b):
    return a * b


def div(b, c):
    return b / c


def getfloatinput(prompt):
    user_input = input(prompt)  # asking for the user to input their answer
    if user_input == "":
        return ""
    while not user_input.isnumeric():  # if the number is not numeric (numbers)
        print("Please ONLY enter a number (an integer to be specific)")  # asking to only enter a number
        user_input = input(prompt)  # re-asking the user's input
    return float(user_input)  # returning the users input


def PhyEq(aName, bName, cName, aUnits, bUnits, cUnits, EQF):
    eq = EQF.split(",")
    equation = f"{eq[0]} = {eq[1]} {eq[3]} {eq[2]}"
    print(eq, equation)
    print("Welcome to Equation Solver, Please press enter on an unknown value to solve for it, enter ")
    a = getfloatinput(f"Please enter {aName} in {aUnits}: ")
    if a == "":
        a = 0
    b = getfloatinput(f"Please enter {bName} in {bUnits}: ")
    if b == "":
        b = 0
    c = getfloatinput(f"Please enter {cName} in {cUnits}: ")
    if c == "":
        c = 0
    if a == 0:
        print(f"{aName} unknown")
        ans = div(b, c)
        print(ans, aUnits)
    if b == 0:
        print(f"{bName} unknown")
        ans = mult(a, c)
        print(ans, bUnits)
    if c == 0:
        print(f"{cName} unknown")
        ans = div(a, b)
        print(ans, cUnits)


if __name__ == "__main__":
  PhyEq("Speed", "Distance", "Time", "m/s", "m", "s", "S,D,T,/")
