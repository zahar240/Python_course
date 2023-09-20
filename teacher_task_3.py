# Пользователь вводит число n. Необходимо вывести первые n чисел Фибоначчи

n = int(input())

f_1 = 0
f_2 = 1

f_n = [0, 1]

for i in range(n - 1):
    i = f_1 + f_2
    f_1, f_2 = f_2, i
    f_n_res = f_n.append(i)

print(f_n)

