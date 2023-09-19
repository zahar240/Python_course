"""Пользователь любым способом вводит несколько чисел. Нужно найти сумму и
произведение этих чисел. Решить двумя способами
"""

nums = []
sum = 0
mult = 1

for i in input().split():
    nums.append(int(i))
    sum += int(i)
    mult *= int(i)

print(sum, mult)