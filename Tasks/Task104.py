# Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random

list1 = [random.randint(1,10) for i in range(10)]
print(list1)
list2 = set(list1)
print(len(list2))