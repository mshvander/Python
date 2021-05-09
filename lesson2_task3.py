#Пользователь вводит месяц в виде целого числа от 1 до 12.
#Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
#Напишите решения через list и через dict.

month = int(input('Введите номер месяца: '))

# через list
winter = (12, 1, 2)
spring = (3, 4, 5)
summer = (6, 7, 8)
autumn = (9, 10, 11)

if winter.count(month):
    print('Время года зима')
elif spring.count(month):
    print('Время года весна')
elif summer.count(month):
    print('Время года лето')
else:
    print('Время года осень')

# через dict
year = {'Зима':[12, 1, 2], 'Весна':[3, 4, 5], 'Лето':[6, 7, 8], 'Осень':[9, 10, 11]}

for key in year:
    if (year.get(key)).count(month):
        print(f'Время года {key}')