#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1
#Two — 2
#Three — 3
#Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
#При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.

eng = ['One', 'Two', 'Three', 'Four']
rus = ['Один', 'Два', 'Три', 'Четыре']

with open('for_task4_1.txt', 'r', encoding='utf-8') as origin, open('for_task4_2.txt', 'w', encoding='utf-8') as target:
    for str_origin in origin:
        for i in range(len(eng)):
            if eng[i] in str_origin:
                str_target = rus[i] + (str_origin[len(eng[i]):])
                target.write(str_target)
