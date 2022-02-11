"""
Welcome to the Python Maths, Physics and Chemistry Calculator

"""

# ---------- IMPORTS ---------- #
import basic_commands
import basic_maths
from basic_commands import avg
from FormulaeSolver import Eqsolve
from art import tprint as tp
from database import get_commands, get_constants, get_eqf
import basic_maths as bm
import memory as mem
import calculus

# ---------- END IMPORTS ---------- #


# ---------- WELCOME ---------- #
tp("Maths - Sci", font="tarty1")  # Ascii art print of first parameter
tp("Calculator", font="4max")
tp("By Choc-a-Block, Sedat Yuksel et al.", font="fancy91")
print("")
# ---------- END WELCOME ---------- #


# ---------- COMMAND LINE ---------- #
exit_cli = False

while not exit_cli:

    print("Please enter command here (enter help to get list of commands)")
    command = input(">>").lower()
    # ---------- EVALUATE COMMAND ---------- #
    if command == "help":
        print("Here is a list of commands: ")
        get_commands()
    elif command == "eqsolve":
        print(Eqsolve.__doc__)  # Prints docstring as a "how-to"
        eqf = get_eqf(input("Please enter equation name: ").lower())
        print(Eqsolve(eqf[0], eqf[1], eqf[2], eqf[3], eqf[4], eqf[5], eqf[6]))
    elif command == "basicmath" or command == "basicmaths":
        bm.basic_maths()
    elif command == "const" or command == "constant" or command == "constants":
        const_request = input("Please enter the constant name you would like to know the value of: ")
        print(get_constants(const_request.lower()))
    elif command == "average" or command == "avg" or command == "averages":
        avg_type = input("Please enter Mean, Median, Mode, or Range as the type of average you would like: ").lower()
        if avg_type == "mean":
            avg_val = avg("mean")
        elif avg_type == "median":
            avg_val = avg("median")
        elif avg_type == "mode":
            avg_val = avg("mode")
        elif avg_type == "range":
            avg_val = avg("range")
        else:
            print("Your input is not a listed average type, Exiting")
        print(f"The {avg_type} is {avg_val}")
        mem.ask_commit(avg_val)
    elif command == "integrate" or command == "integral":
        print(calculus.f.__doc__)
        integrated = calculus.integrate_eq(calculus.f("Integrate"))
        print(integrated)
        mem.ask_commit(integrated)
    elif command == "diff" or command == "differentiate_eq":
        print(calculus.f.__doc__)
        differentiated = calculus.differentiate_eq(calculus.f("Differentiate"))
        print(differentiated)
        solve = input("Would you like to solve for area under the graph? (T/F or Y/N)")
        if solve == "y" or solve == "yes" or solve == "true" or solve == "t":
            ub = basic_commands.get_number_inputS("Please enter the maximum x value of your area: ")
            lb = basic_commands.get_number_inputS("Please enter the minimum x value of your area (same quadrant): ")
            dif_upper = differentiated.sy.subs("x", ub)
        mem.ask_commit(differentiated)
    elif command == "currency" or command == "curr":
        cur_val = basic_commands.currency_convert(basic_commands.get_number_inputS("Please enter Currency value: "),
                                                  input("Please enter that currency's type (GBP, EUR, USD): "),
                                                  out_cur_type := input(
                                                      "Please enter output currency type (GBP, EUR, USD etc): ").upper())
        try:
            cur_val = round(cur_val, 4)
            is_curr = True
        except TypeError:
            is_curr = False
        if out_cur_type == "USD":
            print(f"${cur_val}")
        elif out_cur_type == "EUR":
            print(f"€{cur_val}")
        elif out_cur_type == "GBP":
            print(f"£{cur_val}")
        else:
            if is_curr:
                print(f"{cur_val} {out_cur_type}")
                mem.ask_commit(cur_val)
            else:
                print(cur_val)
    elif command == "quadf" or command == "quadratic formula" or "quadratic" in command:
        print(basic_maths.quad_formula.__doc__)
        x1, x2 = basic_maths.quad_formula()
        if x1 is not None and x2 is None:
            mem.ask_commit(x1)
        elif x1 is not None and x2 is not None:
            mem.ask_commit((x1, x2))
    elif command == "pythag" or "pythag" in command:
        print(basic_maths.trig_pythagoras.__doc__)
        trig_ans = basic_maths.trig_pythagoras()
        print(f"Your result is {trig_ans}")
        mem.ask_commit(trig_ans)
    elif command == "valueconvert" or "convert" in command:
        print(basic_commands.num_type_convert.__doc__)
        value = input("Please enter the value: ")
        value_type = input("Please enter the value type (decimal (or dec, int, den), hex, bin): ").lower()
        out_value_type = input("Please enter the output value type (decimal (or int), hex, bin): ").lower()
        if ("dec" in value_type or "int" in value_type or "den" in value_type) and "bin" in out_value_type:
            outval = basic_commands.num_type_convert(value, "bin-from-den")
        elif "bin" in value_type and ("dec" in out_value_type or "int" in out_value_type or "den" in out_value_type):
            outval = basic_commands.num_type_convert(value, "den-from-bin")
        elif ("dec" in value_type or "int" in value_type or "den" in value_type) and "sci" in out_value_type:
            outval = basic_commands.num_type_convert(value, "sci")
        elif ("dec" in value_type or "int" in value_type or "den" in value_type) and "pretty" in out_value_type:
            outval = basic_commands.num_type_convert(value, "pretty")
        print(f"The output value is: {outval}")
        mem.ask_commit(outval)

# ---------- END EVALUATE COMMAND ---------- #
