#Программа запрашивает у пользователя строку чисел, разделенных пробелом.
#При нажатии Enter должна выводиться сумма чисел.
#Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
#Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
#Но если вместо числа вводится специальный символ, выполнение программы завершается.
#Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме
#и после этого завершить программу.

def my_func(sum_final, *args):
    '''Считает сумму введенных чисел

    sum - сумма чисел во введенной строке
    sum_final - сумма чисел во всех введенных строках
    '''
    sum = 0
    for i in list:
        sum = sum + int(i)
    sum_final = sum_final + sum
    print(f'Промежуточная сумма {sum}. Общая сумма {sum_final}.')
    return sum_final

sum_final = 0

while True:
    break_the_loop = False
    str = input('Вводите числа через пробел. Enter - подсчет суммы, q - выход из программы: ')
    list = str.split()
    for i in list:
        if not i.isdigit() and i.upper() != 'Q':
            print('Введен недопустимый символ!')
            break_the_loop = True
            break
    if break_the_loop:
        continue
    if list.count('q'):
        list.pop()
        sum_final = my_func(sum_final, list)
        break
    sum_final = my_func(sum_final, list)
