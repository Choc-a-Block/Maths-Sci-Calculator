from statistics import median, mean, mode

from currency_converter import CurrencyConverter


def touch_up(Input_String):  # function touch_up taking the parameter of the question and putting it in Input_string
    str1 = str(Input_String).replace('[', '').replace(']', '')  # removing []
    str2 = str(str1).replace(',', '').replace("'", '')  # removing , and '
    return str(str2).replace('(', '').replace(")", '')  # removing () and returning


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


def get_number_inputS(prompt):  # S for strict (does not allow any other input, only int or float)
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


def get_number_inputL(prompt):  # L for lenient (allows anything else and returns "" if not int/float)
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


def avg(avg_type):  # Takes in Average Type as Str of "mean", "median", "mode", "range"
    """Asks user for values until they dont enter an integer or float. This will return the Mean, Median, Mode or Range as Int or Float"""
    itemlist = []
    print(f"-- {avg_type} selected --")
    user_in = get_number_inputL("Please enter a number (Int or Float) to add to the list to average: ")
    print("-- At any point, enter anything other than an Int or Float to average --")
    while user_in != "":
        itemlist.append(user_in)
        user_in = get_number_inputL("Please enter the next number: ")
    if avg_type == "mean":
        return mean(itemlist)  # Returns Mean as Int or Float
    elif avg_type == "median":
        return median(itemlist)  # Returns Median of list as Int or Float
    elif avg_type == "mode":
        return mode(itemlist)  # Returns Mode as Int or Float
    elif avg_type == "range":
        return max(itemlist) - min(itemlist)  # returns range as Int or Float


def num_type_convert(value, format_V):
    """Welcome to Number Converter: Enter a value, and its format. Enter your output format and We will handle the rest. You can convert to scientific notation, Hexadecimal, Binary and back to Deanery. You can also convert to 'pretty' format, separating big values with commas and rounding to 2dp."""
    return_val = 0
    if format_V == "sci":
        return_val = format(value, "10e")
    elif format_V == "pretty":
        if type(value) == int:
            return_val = format(value, ",")
        else:
            return_val = format(float(value), ",.2f")
    elif format_V == "bin-from-den":
        return_val = bin(int(value)).replace("00b", "").replace("0b", "")
    elif format_V == "hex-from-den":
        return_val = int(value, 16)
    elif format_V == "den-from-bin":
        return_val = '{0:b}'.format(int(value, 2))
    return str(return_val)


def currency_convert(value, value_curr, target_curr):
    """Welcome to Currency Converter: This program uses live currencies to convert your value to any supported currency. Enter your value, its currency and the wanted output currency below: """
    c = CurrencyConverter()
    
    try:
        return c.convert(value, value_curr, target_curr)
    except ValueError or TypeError:
        return f"Sorry, but we currently do not support either {value_curr} or {target_curr}, please try again"
