field = [
    ['-','-','-',],
    ['-','-','-',],
    ['-','-','-',]]


def show_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i), *field[i])


def user_input(f):
    while True:
        place = input(f'Ходит {user}. Введите координаты: ').split()
        if len(place) != 2:
            print('Введите две координаты!')
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print('Введите числа!')
            continue
        x, y = map(int, place)
        if not (x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Выход из диапазона!')
            continue
        if f[x][y] != '-':
            print('Клетка занята!')
            continue
        break
    return x, y


def win(f, user):
    def check(a1, a2, a3, user):
        if a1 == user and a2 == user and a3 == user:
            return True
    for n in range(3):
        if check(f[n][0], f[n][1], f[n][2], user) or \
                check(f[0][n], f[1][n], f[2][n], user) or \
                check(f[0][0], f[1][1], f[2][2], user) or \
                check(f[2][0], f[1][1], f[0][2], user):
            return True
    return False


count = 0
while True:
    if count == 9:
        print('Ничья')
        break
    if count % 2 == 0:
        user = 'x'
    else:
        user = 'o'
    show_field(field)
    x, y = user_input(field)
    field[x][y] = user
    if win(field, user):
        print(f'Выйграл {user}!')
        show_field(field)
        break
    count += 1
