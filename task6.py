start = float(input('Введите дистанцию первого дня: '))
target = float(input('Введите дистанцию-цель: '))
day = 1

while start < target:
    start = start * 1.1
    day += 1

print(f'Спортсмен достигнет результата на день № {day}')