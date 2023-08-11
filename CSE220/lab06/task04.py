#part A
def printnum(num):

    if num == 0:
        return
    printnum(num-1)
    print(num, end=' ')

def print_pattern(n , i):
    if n == 0:
        return
    printnum(i)
    print('\n', end='')
    print_pattern(n-1, i+1)

n = 5
print_pattern(n,1)
#part B
def forward(i, n):
    if i == n+1:
        print()
        return
    print(i, end=" ")
    return forward(i+1, n)

def number(num, col, j):
    if col == j-1:
        return
    print(" ", end=" ")
    return number(num, col-1, j)

def pattern(num , col):
    if num == 0:
        return
    number(num, num-col, 1)
    forward(1, col)
    pattern(num, col+1)
    if col == num-1:
        forward(1, col+1)

pattern(5, 1)