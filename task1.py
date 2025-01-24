def get_sum(my_file_name):
    numbers_list = list()
    tot_sum = 0
    f = open(my_file_name, 'r', encoding='utf-8')
    rows_list = f.readlines() # список строк в текстовом режиме
    for row in rows_list:
        numbers_list.append(row.split())
    
    print(numbers_list)
        
    for number in numbers_list:
        print(number)
        tot_sum += int(*number)
    
    f.close()
    
    return tot_sum

def write_sum(my_file_name, value):
    f = open(my_file_name, 'w', encoding='utf-8')
    f.write(value)
    f.close()

my_sum = get_sum('numbers.txt')
print(my_sum)
write_sum('answers.txt', str(my_sum))