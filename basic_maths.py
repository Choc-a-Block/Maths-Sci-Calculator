from basic_commands import get_number_inputL, get_number_inputS
import memory as mem
from math import sqrt


def basic_maths():
    c = False
    while not c:
        try:
            ans = eval(input("Please enter basic maths calculation with numbers, operators and brackets ONLY: "))
            print(ans)
            mem.ask_commit(ans)
            c = True
        except:
            print(
                "That was not in the format requested, Please only use basic operators '*, /, -, +' and integers or floats")


def quad_formula():
    """Welcome to the Quadratic Formula tool. Enter coefficients a, b, and c to solve for x using the Quadratic Formula (where ax^2 + bx + c = 0)"""
    a = get_number_inputS("Enter the coefficient of a: ")
    b = get_number_inputS("Enter the coefficient of b: ")
    c = get_number_inputS("Enter the coefficient of c: ")
    d = b ** 2 - 4 * a * c  # discriminant
    if d < 0:
        print("This equation has no real solution")
        return None, None
    elif d == 0:
        x = (-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
        print(f"This equation has one solution: {x}")
        return x, None
    else:
        x1 = (-b + sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
        x2 = (-b - sqrt((b ** 2) - (4 * (a * c)))) / (2 * a)
        print(f"This equation has two solutions: {x1} or {x2}")
        return x1, x2


def trig_pythagoras():
    """Welcome to the Pythagoras theorem calculator. Enter values a, b and c to be used in the formula: a^2 + b^2 = c^2. Enter anything nothing for an unknown value (it solves for that)"""
    a, b, c = get_number_inputL("Enter coefficient a: "), \
              get_number_inputL("Enter coefficient b: "), \
              get_number_inputL("Enter coefficient c: ")
    try:
        if c == "":
            answer = sqrt(a ** 2 + b ** 2)
        elif b == "":
            answer = sqrt(c ** 2 - a ** 2)
        elif a == "":
            answer = sqrt(c ** 2 - b ** 2)
        else:
            answer = "Incorrect Input, Please try again"
    except ValueError:
        answer = "That is incalculable... one of your values is too large: Please try again"
    return answer
