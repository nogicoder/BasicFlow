def concat_files(*args):
    concat_list = " "
    for file_name in args:
        file = open(file_name, "r")
        if file == None:
            continue
        # content = file.read(file)
        content = file.read()
        concat_list += content
        file.close()
    concatenated_files = open("concatenated_files", "w+")
    concatenated_files.write(concat_list)
    concatenated_files.close()
    concatenated_files = open("concatenated_files", "r")
    concat_content = concatenated_files.read()
    concatenated_files.close()
    return concat_content

print(concat_files("toto.txt", "tutu.txt", "titi.txt"))
