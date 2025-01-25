
def get_back_list(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        init_list = list()
        init_list = f.readlines()
        value = len(init_list)
        for i in reversed(range(value)):
            print(init_list[i])

my_file_name = 'PythonDzen.txt'
get_back_list(my_file_name)