#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def person_info(**kwargs):
    '''Принимает данные пользователя'''
    return kwargs

list = ['Имя', 'Фамилия', 'Год рождения', 'Город проживания', 'Электронная почта', 'Телефон']
per = []
num = 0

for i in list:
    a = input(f'Введите значение параметра {list[num]}: ')
    per.append(a)
    num +=1

info = person_info(name = per[0], surname = per[1], year_of_birth = per[2],city_of_residence = per[3], email = per[4], phone = per[5])

num = 0
for key in info:
    print(f'{list[num]} - {info.get(key)}, ', end = '')
    num += 1
