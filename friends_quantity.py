start = 1
stop = input("Сколько у Вас друзей?: ")
stop = int(stop)
i = start
friends_names = []


while i <= stop:
    name = input(f"Введите имя друга {i}: ")
    i += 1
    friends_names.append(name.title())


print(f"Ваши друзья: {friends_names}")
