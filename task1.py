# это решение годится только для случаев, когда в каждой из строк записано только по одному числу
def get_sum(my_file_name):
    numbers_list = list()
    tot_sum = 0
    with open(my_file_name, 'r', encoding='utf-8') as f:
        rows_list = f.readlines() # списки строк в текстовом режиме
        for row in rows_list:
            numbers_list.append(*row.split()) # распаковываем каждый из списков
        
        for number in numbers_list:
            tot_sum += int(number)
    
    return tot_sum

def write_sum(my_file_name, value):
    with open(my_file_name, 'w', encoding='utf-8') as f:
        f.write(str(value))

my_sum = get_sum('numbers.txt')
write_sum('answers.txt', my_sum)