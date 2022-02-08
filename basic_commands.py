def touch_up(Input_String):  # function touch_up taking the parameter of the question and putting it in Input_string
    str1 = str(Input_String).replace('[', '').replace(']', '')  # removing []
    str2 = str(str1).replace(',', '').replace("'", '')  # removing , and '
    return str(str2).replace('(', '').replace(")", '')  # removing () and returning