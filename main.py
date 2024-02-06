squares = [i**2 for i in range(1,11)]
#квадрат первых 10 натуральных чисел
squares = [i**2 for i in range(1,11) if i % 2 == 1]
#нечётные
list_tuples = [(i, i**2) for i in range(1,11)]
#список из кортежей
M = [[i+j for j in range(5)] for i in range(5)]
#матрица
T = [[i*j for j in range(1,11)] for i in range(1,11)]
print(T, sep="\n")
#таблица умножения чисел от 1 до 10
L = [int(input()) % 2 == 0 for i in range(5)]
print( any(L)) #хотя бы одно чётное число то будет тру

L = [i for i in range(10)]
# 0 1 2 3 4 5 6 7 8 9
M = [i for i in range(10,0,-1)]
# 10 9 8 7 6 5 4 3 2 1
for a in zip(L,M): #Мы создаем новый список из двух прошлых
    print(a)

for a, b in zip(L,M):
    print('a =', a, 'b =', b) #можно ещё приятнее для глаза

N = [a * b for a, b in zip(L, M)] #произведение элементов списка