function_names = []

with open("temp.py", 'rb') as f:
    for line in f.readlines():
        line = str(line).strip()
        print(type(line))
        print(line)
        if str(line).startswith('def'):
            function_name = line.split(' ')[1]
            function_names.append(function_name)

print(function_names)
