"""
Welcome to the Python Maths, Physics and Chemistry Calculator
Below is listed a plethora of equations and calculations that you can use, and how to use them.

"""

# ---------- IMPORTS ---------- #
# import math
# import random
from FormulaeSolver import Eqsolve
# import pandas as pd
# import scipy as sp
# import numpy as np
# import sympy as sy
import art
import database as db
import BasicMaths as bm
# import basic_commands as bc

# ---------- END IMPORTS ---------- #

# ---------- FUNCTIONS ---------- #

# ---------- END FUNCTIONS ---------- #


# ---------- WELCOME ---------- #
print("Welcome to:")
art.tprint("Maths - Sci", font="4max")  # Ascii art print of first parameter
art.tprint("Calculator", font="4max")
# ---------- END WELCOME ---------- #


# ---------- COMMAND LINE ---------- #
exit_cli = False

while not exit_cli:

    print("Please enter command here (enter help to get list of commands)")
    command = input(">>").lower()

    # ---------- EVALUATE COMMAND ---------- #
    if command == "help":
        print("Here is a list of commands: ")
        db.getcommands()
    elif command == "eqsolve":
        print(Eqsolve.__doc__)
        eqf = db.geteqf(input("Please enter equation name: "))
        print(Eqsolve(eqf[0], eqf[1], eqf[2], eqf[3], eqf[4], eqf[5], eqf[6]))
    elif command == "basicmath" or command == "basicmaths":
        bm.basic_maths()
# ---------- END EVALUATE COMMAND ---------- #
