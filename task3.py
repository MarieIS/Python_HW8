def read_list(my_file_name):
    res_list = list()
    with open(my_file_name, 'r', encoding='utf-8') as f:
        rows_list = list()
        rows_list = f.readlines()
        list_count = int(*rows_list[0].split())
        for row in range(1, len(rows_list)):
            info_list = list()
            info_list = rows_list[row].split()
            if int(info_list[2]) > list_count:
                res_list.append(info_list)
    return res_list

def write_list(my_file_name, input_list):
    input_list.sort(key=lambda i: i[2], reverse=True)
    with open(my_file_name, 'w', encoding='utf-8') as f:
        for row in range(len(input_list)):
            string = str(row+1) + ') ' + input_list[row][1][0] + '. ' + input_list[row][0] + ' ' + str(input_list[row][2]) + '\n'
            f.write(string)

my_list = read_list('first_tour.txt')
write_list('second_tour.txt', my_list)