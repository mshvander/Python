#Создать текстовый файл (не программно), сохранить в нем несколько строк,
#выполнить подсчет количества строк, количества слов в каждой строке.

with open('lyrics.txt', 'r') as f:
    content = f.readlines()

print('Всего строк в файле: ', len(content))
i = 1

for line in content:
    line_word = line.split(' ')
    print(f'Строка №{i}: количество слов - {len(line_word)}')
    i += 1
