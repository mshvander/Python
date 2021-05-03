number = int(input('Введите целое положительное число: '))
# digit - цифра в числе
# depth - глубина разрядности введенного числа
# max - максимальная цифра в числе
max = 0

while True:
    digit = number % 10
    if digit>max:
        max = digit
    depth = number // 10
    if depth == 0:
        break
    number = depth


print(f'Максимальная цифра в числе: {max}')
