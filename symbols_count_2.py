string = input("Введите строку: ")
checked = ""
for symbol in string:
    if symbol not in checked:
        counter = string.count(symbol)
        print(symbol, counter)
        checked += symbol
