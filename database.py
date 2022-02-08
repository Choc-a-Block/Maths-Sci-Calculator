from csv import reader
import basic_commands as bc

def geteqf(eqpointer):
    with open('equations.csv', 'r') as read_obj:
        csv_reader = reader(read_obj)  # pass the file object to reader() to get the reader object
        list_of_rows = list(csv_reader)  # Pass reader object to list() to get a list of lists
        for i in range(len(list_of_rows)):
            if eqpointer in list_of_rows[i]:
                return list_of_rows[i]

def getcommands():
    raw_commands = []
    ref = []
    with open("commands.txt", "r") as commandfile:
        lines = commandfile.readlines()
        for line in lines:
            raw_commands.append(line)
    for x in raw_commands:
        ref.append(x.replace("\n", ""))
    ref_commands = bc.touch_up(str(ref))
    list_commands = ref_commands.split(" ")
    for cmd in range(len(list_commands)):
        print(list_commands[cmd])