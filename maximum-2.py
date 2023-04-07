start = 1
stop = input("Введите кол-во чисел: ")
stop = int(stop)
i = start
a = 0


while i <= stop:
    number = input(f"Введите число {i}: ")
    number_int = int(number)
    i += 1
    if number_int > a:
        a = number_int

print(f"Максимальное число: {a}")
