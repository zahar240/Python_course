#Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = int(input())
k = 0

while 2 ** k < n:
    print(2 ** k, end=" ")
    k += 1 