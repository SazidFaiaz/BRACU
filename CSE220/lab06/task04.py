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
