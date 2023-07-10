import numpy as np


def creat_amtrix():

    m = np.zeros((2,3), dtype= int)
    print(m)
    for i in range(2):
        for j in range(3):
            print(f'inter value of [{i}][{j}] index:')
            m[i][j] = int(input())

    return m

print(creat_amtrix())