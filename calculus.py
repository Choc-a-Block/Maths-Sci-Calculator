from sympy import *


def differentiate_eq(equation):
    x = symbols("x")
    return diff(equation, x)


def f(EQ_type):
    """Welcome to Calculus Tool. Use 4*x instead of 4x, ** or ^ for power, and sqrt() for Square Root. use sin(), cos(), and tan() for Sine, Cosine, and Tangent"""
    equation = sympify(input(f"Enter f(x) to {EQ_type}:").replace("^", "**"))
    return equation


def integrate_eq(eq):
    return integrate(eq, symbols("x"))


if __name__ == '__main__':
    # print(integrate_eq(f("Integrate")))
    print(differentiate_eq(f("Differentiate")))
