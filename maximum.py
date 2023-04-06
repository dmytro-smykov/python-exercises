start = 1
stop = input("Введите кол-во чисел: ")
stop = int(stop)
i = start
all_numbers = []


while i <= stop:
    number = input(f"Введите число {i}: ")
    number_int = int(number)
    i += 1
    all_numbers.append(number_int)


max_number = max(all_numbers)
print(f'Максимальное число: {max_number}')
