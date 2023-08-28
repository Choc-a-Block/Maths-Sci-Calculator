import Memory as mem


def basic_maths():
    c = False
    while not c:
        try:
            ans = eval(
                input(
                    "Please enter basic maths calculation with numbers, operators and brackets ONLY: "
                )
            )
            print(ans)
            commit = input("Commit to Memory? T/F or Y/N: ").lower()
            if commit == "y" or commit == "t" or commit == "yes" or commit == "true":
                mem.commit_to_mem(ans)
            c = True
        except:
            print(
                "That was not in the format requested, Please only use basic operators '*, /, -, +' and integers or floats"
            )
