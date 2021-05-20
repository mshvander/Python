#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def file_sum(file):
    sum  = 0
    with open(file, 'r') as f:
        numbers = (f.read()).split(' ')
        for el in numbers:
            sum = sum + int(el)
    return sum

with open('for_task5.txt', 'w') as f:
    f.write(input('Введите числа через пробел: '))

print(file_sum('for_task5.txt'))
