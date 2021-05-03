revenue = float(input('Введите значение выручки: '))
costs = float(input('Введите значение издержек: '))
profit = revenue - costs

if profit>0:
    print(f'Вы сработали с прибылью {profit}')
    print(f'Рентабельность: {(profit / revenue) * 100} %')
    staff = int(input('Введите количество сотрудников: '))
    print(f'Прибыль в расчете на одного сотрудника составляет: {profit / staff}')
elif profit<0:
    print(f'Вы сработали с убытком {profit}')
else:
    print('Вы сработали в ноль.')
