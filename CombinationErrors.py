name_file = input("Введите имя файла")

try:
    f = open(name_file, "r")
    data = f.readlines()
    data = list(map(int, data))

except FileNotFoundError:
    print("Файл не найден!")
except ValueError:
    print("Ошибка в формате данных в файле")
else:
    print(data)
finally: # этот блок выполняется ВСЕГДА, и когда есть ошибка, и когда нет ошибки
    print("Программа завершена!")
