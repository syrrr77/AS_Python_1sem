# Ввод строки и значения n
cr7 = input("Введите строку: ")
n = int(input("Введите n: "))

# Создаём новую строку, пропуская  n-ые символы
final = ""

for i in range(len(cr7)):
    if (i + 1) % n != 0:
        final += cr7[i]

print("Результат: ", final)
