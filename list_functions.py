import sys
from code import interact

def get_code(file_path):
    with open(file_path, "r") as f:
        code = f.read().split("\n")
    return code

def get_functions(code):
    functions = []
    for line in code:
        if "def " in line:
            try:
                functions.append(line.split()[1])
            except:
                interact(local=locals())
    return functions

if __name__ == '__main__':
    first_file = sys.argv[1]
    second_file = sys.argv[2]
    code_one = get_code(first_file)
    code_two = get_code(second_file)
    functions_one = get_functions(code_one)
    functions_two = get_functions(code_two)
    for func in functions_one:
        if func in functions_two:
            print(func)
