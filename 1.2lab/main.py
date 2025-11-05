# Ввод значений A, B и H
A = float(input("Введите значение A: "))
B = float(input("Введите значение B: "))
H = float(input("Введите шаг H: "))

# Итерация по диапазону с шагом H
now = A
while now <= B:
    if now > 0:
        print(now)
    now += H
