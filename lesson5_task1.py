#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных свидетельствует пустая строка.

def file_creation(name):
    with open(f'{name}', 'w', encoding='utf-8') as f:
        while True:
            s = input('Ввод данных: ')
            if s == '':
                break
            f.write(f'{s}\n')

def file_creation_2(name):
    list = []
    while True:
        str = input('И еще немного данных: ') + '\n'
        if str == '\n':
            break
        list.append(str)
    with open(f'{name}', 'a', encoding='utf-8') as f:
        f.writelines(list)

name = input('Введите имя файла: ') + '.txt'

file_creation(name) # Первый вариант.
file_creation_2(name) # Второй вариант.
