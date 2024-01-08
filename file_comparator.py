def get_part (string):
    line = string.split(";")
    return (str(line[0]))

def is_on_the_list (list, string):
    for line in list:
        line = get_part(line)
        if string == line:
            return True

def get_file (list1, list2, logs):
    list_for_file = []
    for j in list1:
        first_string = get_part(j)
        for k in list2:
            second_string = get_part(k)
            if first_string == second_string:
                list_for_file.append(k)
                logs.append(j + " > " + k)
        if is_on_the_list (list_for_file, first_string) != True:
            list_for_file.append(j)
    return list_for_file 

def get_list (text):
    lines = []
    with open(text) as file:
        for line in file: 
            line = line.strip()
            lines.append(line) 
    return lines

old_file = get_list(r"old file.txt")
new_file = get_list(r"new file.txt")
logs = []
fixed_file = get_file(old_file, new_file, logs)

with open(r'file from script.txt', 'x') as fp:
    for item in fixed_file:
        fp.write("%s\n" % item)

with open(r'logs.txt', 'x') as fp:
    for item in logs:
        fp.write("%s\n" % item)



