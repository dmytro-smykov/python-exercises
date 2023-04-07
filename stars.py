start = 1
insert_x = (input("Введите кол-во x: "))
x_int = int(insert_x)

insert_y = (input("Введите кол-во y: "))
y_int = int(insert_y)

i_x = start
i_y = start

symbols_x = []


while i_x <= x_int:
    i_x += 1
    symbols_x.append('*')

while i_y <= y_int:
    i_y += 1
    print(''.join(symbols_x))
