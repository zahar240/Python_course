"""На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
"""
from random import randint

n = int(input())
coins = []

for i in range(n):
    coins.append(randint(0, 1))
print(coins)

zero = coins.count(0)
one = coins.count(1)

if zero > one:
    print(one)
else:
    print(zero)