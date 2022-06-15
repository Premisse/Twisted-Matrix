# Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали,
# выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
# Sample Input:
# 5
# Sample Output:
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

NUMBER = int(input("Input number: "))
FINALLY_NUMBER = NUMBER * NUMBER

matrix = [[i for i in range(NUMBER)] for j in range(NUMBER)]

counter = 1
x = 0
y = 0
c = 1
dx = 0
dy = 0

while counter <= FINALLY_NUMBER:
    if counter == FINALLY_NUMBER:
        if NUMBER % 2 != 0:
            matrix[x-1][y-1] = counter
            break
        else:
            matrix[x][y] = counter
            break

    y = dy
    x = dx
    x_rev = NUMBER - c
    y_rev = NUMBER - c

    for _ in matrix[x]:
        while y != y_rev:
            matrix[x][y] = counter
            y += 1
            counter += 1

    for _ in matrix[x]:
        while x != x_rev:
            matrix[x][y_rev] = counter
            x += 1
            counter += 1

    for _ in matrix[x]:
        while y_rev != dy:
            matrix[x][y_rev] = counter
            y_rev -= 1
            counter += 1
    dy += 1

    for _ in matrix[x]:
        while x_rev != dx:
            matrix[x_rev][y_rev] = counter
            x_rev -= 1
            counter += 1
    dx += 1
    c += 1

for n in matrix:
    for m in n:
        print(m, end="   ")
    print()