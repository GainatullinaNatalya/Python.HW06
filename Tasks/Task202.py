# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.

N = int(input('Введите количество друзей: '))
friend1 = dict([input('Введите имя и возраст через пробел:').split() for i in range(N)])
friend2 = {k: int(v) for k, v in friend1.items()}
for i, j in friend2.items():
    if j == min(friend2.values()):
        print(i)