"""
Welcome to the Python Maths, Physics and Chemistry Calculator

"""

from art import tprint as tp

from FormulaeSolver import Eqsolve
# ---------- IMPORTS ---------- #
from basic_commands import num_type_convert, get_number_inputS, currency_convert, avg
from basic_maths import basic_maths
from basic_maths import quad_formula, trig_pythagoras
from calculus import differentiate_eq, f, integrate_eq
from database import get_contents, get_constants, get_eqf, get_currencies
from memory import Memory

# ---------- END IMPORTS ---------- #


# ---------- INIT + Welcome ---------- #
Session_Memory_Object = Memory()
tp("Maths - Sci", font="tarty1")  # Ascii art print of first parameter
tp("Calculator", font="4max")
tp("By Choc-a-Block, Sedat Yuksel et al.", font="fancy91")
print("")
# ---------- END INIT + WELCOME ---------- #


# ---------- COMMAND LINE ---------- #
exit_cli = False

while not exit_cli:

    print("Please enter command here (enter help to get list of commands)")
    command = input(">>").lower()
    # ---------- EVALUATE COMMAND ---------- #
    match command:
        case "help":
            print("Here is a list of commands: ")
            get_contents("commands.txt")
        case "eqsolve" | "physics" | "physics solver":
            print(Eqsolve.__doc__)  # Prints docstring as a "how-to"
            eqf = get_eqf(input("Please enter equation name: ").lower())
            print(Eqsolve(eqf[0], eqf[1], eqf[2], eqf[3], eqf[4], eqf[5], eqf[6]))
        case "basicmath" | "basicmaths":
            basic_maths_ans = basic_maths()
            print(basic_maths_ans)
            Session_Memory_Object.ask_commit(basic_maths_ans, "basicmaths")
        case "const":
            const_request = input("Please enter the constant name you would like to know the value of: ")
            print(get_constants(const_request.lower()))
        case "average" | "avg":
            avg_type = input("Please enter Mean, Median, Mode, or Range as the type of average you would like: ").lower()
            match avg_type:
                case "mean":
                    avg_val = avg("mean")
                case "median":
                    avg_val = avg("median")
                case "mode":
                    avg_val = avg("mode")
                case "range":
                    avg_val = avg("range")
                case _:
                    print("Your input is not a listed average type, Exiting")
                    break
            print(f"The {avg_type} is {avg_val}")
            Session_Memory_Object.ask_commit(avg_val, "average")
        case "integrate" | "integral":
            print(f.__doc__)
            integrated = integrate_eq(f("Integrate"))
            print(integrated)
            Session_Memory_Object.ask_commit(integrated, "integrate")
            """
            solve = input("Would you like to solve for area under the graph? (T/F or Y/N)")
            if solve == "y" or solve == "yes" or solve == "true" or solve == "t":
                ub = basic_commands.get_number_inputS("Please enter the maximum x value of your area: ")
                lb = basic_commands.get_number_inputS("Please enter the minimum x value of your area (same quadrant): ")
                dif_upper = differentiated.sy.subs("x", ub)
            """
        case "diff" | "differentiate":
            print(f.__doc__)
            differentiated = differentiate_eq(f("Differentiate"))
            print(differentiated)
            Session_Memory_Object.ask_commit(differentiated, "differentiate")
        case "currency" | "curr":
            print(currency_convert.__doc__)
            get_curr_types = input("Would you like to get a list of currencies we currently support? T/F or Y/N: ").lower()
            if get_curr_types == "y" or get_curr_types == "t" or get_curr_types == "yes" or get_curr_types == "true":
                get_contents("supported_currencies.txt")
            cur_val = currency_convert(get_number_inputS("Please enter Currency value: "),
                                       input("Please enter that currency's type (GBP, EUR, USD): ").upper(),
                                       out_cur_type := input("Please enter output currency type (GBP, EUR, USD etc): ").upper())
            try:
                cur_val = round(cur_val, 4)
                is_curr = True
            except TypeError:
                is_curr = False
            match out_cur_type:
                case "USD":
                    print(f"${cur_val}")
                case "EUR":
                    print(f"€{cur_val}")
                case "GBP":
                    print(f"£{cur_val}")
                case _:
                    if is_curr:
                        print(f"{cur_val} {out_cur_type}")
                        Session_Memory_Object.ask_commit(cur_val, "currency")
                    else:
                        print(cur_val)
        case "quadf" | "quadratic formula" | "quadratic":
            print(quad_formula.__doc__)
            x1, x2 = quad_formula()
            if x1 is not None and x2 is None:
                Session_Memory_Object.ask_commit(x1, "quadratic_f")
            elif x1 is not None and x2 is not None:
                Session_Memory_Object.ask_commit((x1, x2), "quadratic_f")
        case "pythag" | "pythag":
            print(trig_pythagoras.__doc__)
            trig_ans = trig_pythagoras()
            print(f"Your result is {trig_ans}")
            Session_Memory_Object.ask_commit(trig_ans, "pythagoras")
        case "valueconvert" | "convert" | "currency convert":
            print(num_type_convert.__doc__)
            value = input("Please enter the value: ")
            value_type = input("Please enter the value type (decimal (or dec, int, den), hex, bin): ").lower()
            out_value_type = input("Please enter the output value type (decimal (or int), hex, bin): ").lower()
            if ("dec" in value_type or "int" in value_type or "den" in value_type) and "bin" in out_value_type:
                outval = num_type_convert(value, "bin-from-den")
            elif "bin" in value_type and ("dec" in out_value_type or "int" in out_value_type or "den" in out_value_type):
                outval = num_type_convert(value, "den-from-bin")
            elif ("dec" in value_type or "int" in value_type or "den" in value_type) and "sci" in out_value_type:
                outval = num_type_convert(value, "sci")
            elif ("dec" in value_type or "int" in value_type or "den" in value_type) and "pretty" in out_value_type:
                outval = num_type_convert(value, "pretty")
            print(f"The output value is: {outval}")
            Session_Memory_Object.ask_commit(outval, "currency_conversion")
        case "currency_hist" | "hist":
            print(get_currencies.__doc__)
            curr_hist = get_currencies("CurrencyValues_new.csv")

# ---------- END EVALUATE COMMAND ---------- #
