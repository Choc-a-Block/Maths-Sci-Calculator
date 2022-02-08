def commit_to_mem(value):
    with open("memory.txt", "a+") as file_object:
        file_object.seek(0)  # seek to beginning of file
        data = file_object.read(100)  # read 100 terms
        if len(data) > 0:  # if there is data in it
            file_object.write("\n")  # add newline
        file_object.write(str(value))  # write value & close
        

if __name__ == "__main__":
    commit_to_mem(4)