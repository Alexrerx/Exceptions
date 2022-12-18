try:
    a = int(input("Введите первое число"))
    b = int(input("Введите первое число"))
except ValueError:
    print("Неверный ввод!")
else:
    print(a + b)
