# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.

N = int(input('Введите количество друзей: '))
friend1 = dict([input('Введите имя и возраст через пробел:').split() for i in range(N)])
friend2 = {k: int(v) for k, v in friend1.items()}
for i, j in friend2.items():
    summ = sum(friend2.values()) / N
    maxx = max(friend2.keys(), key=len)
print(summ, maxx, sep='\n')