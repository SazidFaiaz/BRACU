
filein = open("input01A.txt", "r")
fileout = open("output01A.txt", "w")

N, M = map(int, filein.readline().split())
print(N, M)

matrix = [[0] * (N + 1) for _ in range(N + 1)]
for i in range (M):
    u, v, w = map(int, filein.readline().strip().split(" "))
    print(u, v, w)
    matrix[u][v] = w
# print(matrix)

def printmatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
            fileout.write(f'{matrix[i][j]}')
        fileout.write(f'\n')
        print()

printmatrix(matrix)