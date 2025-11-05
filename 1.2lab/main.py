# Ввод значений A, B и H
A = float(input("Введите A: "))
B = float(input("Введите B: "))
H = float(input("Введите H: "))

# Проходим по диапазону и выводим только положительные числа
x = A
while x <= B:
    if x > 0:
        print(x)
    x += H
