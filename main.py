name = input("Введите имя файла")
try:
    f = open(name, "r")
except FileNotFoundError:
    print("Файл не найден!")
else:
    print(f.readlines())
    f.close()
