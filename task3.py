number = int(input('Введите число от 1 до 9: '))
while number<1 or number>9:
        number = int(input('Неправильное число! Введите число от 1 до 9: '))

result = number*3 + number*20 + number*100
print(f'{number} + {number}{number} + {number}{number}{number} = {result}')