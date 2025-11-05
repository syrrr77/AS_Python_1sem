# Создание списка
ronaldo = [int(x) for x in input("Введите элементы списка через пробел: ").split()]

# Находим максимум и его индекс в списке
max_ron= max(ronaldo)
max_index = ronaldo.index(max_ron)

# Получаем список элементов справа от максимального без него
right_part = ronaldo[max_index+ 1:]

# Вычисляем произведение элементов справа
product= 1
for num in right_part:
    product*=num

# Если справа нет элементов, произведение = 1
print("Произведение элементов справа от максимального = :", product)
