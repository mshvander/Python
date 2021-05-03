user_seconds = int(input('Введите время в секундах: '))

hours = user_seconds // 3600
minutes = (user_seconds - hours*3600) // 60
seconds = (user_seconds - hours*3600) % 60

print(f'Время в формате чч:мм:сс - {hours}:{minutes}:{seconds}')

# Как сделать чтобы показывало нулевые разряды? Например: не 1:2:16, а 01:02:16?