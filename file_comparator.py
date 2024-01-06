def get_part (string):
    line = string.split(";")
    return (str(line[0]))

def get_file (list1, list2):
    list_for_file = []
    for j in list1:
        first_string = get_part(j)
        for k in list2:
            second_string = get_part(k)
            print(first_string)
            print(second_string)
            if first_string == second_string:
                j = k
                list_for_file.append(j)
            #else:
                #list_for_file.append(j)
            print (list_for_file)
    return list_for_file
                

def get_list (text):
    lines = []
    with open(text) as file:
        for line in file: 
            line = line.strip()
            lines.append(line) 
    return lines

old_file = get_list(r"old_file.txt")
new_file = get_list(r"new_file.txt")

fixed_file = get_file(old_file, new_file)
#print (fixed_file)


