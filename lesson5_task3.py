#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#Выполнить подсчет средней величины дохода сотрудников.

with open('staff.txt', 'r', encoding='utf-8') as f:
    content = f.readlines()

i = 0

for el in content:
    el_suff = el.removesuffix('\n')
    person = el_suff.split(' ')
    person[1] = int(person[1])
    i = i + person[1]
    if person[1] < 20000:
        print(f'Оклад менее 20 тыс.: {person[0]}')

print(f'Средняя величина дохода: {(i/len(content)):.2}')
