
def iteration(array):
    for i in range(len(array)):
        print(array[i])

def revers_iterate(array):
    for i in range(len(array)-1, -1, -1):
        print(array[i])


def coppy_array(array):
    new = [None]*len(array)
    for i in range(len(array)):
        new[i] = array[i]
    return new

def resize_array(aray, newlen):
    newarray = [None] * newlen
    for i in range(len(aray)):
        newarray[i] = aray[i]
    return newarray

def revers_outplace(array):
    revers_array = [None]*len(array)
    count = 0
    j = len(array)-1
    while count < len(array):
        revers_array[count] = array[j]
        count += 1
        j -= 1
    return revers_array


def revers_inplace(array):
    count = 0
    j = len(array) - 1
    while count < j:
        temp = array[count]
        array[count] = array[j]
        array[j] = temp
        count += 1
        j -= 1
    return array

def left_shift(array):
    for i in range(1, len(array)):
        array[i-1] = array[i]
    array[len(array) - 1] = None
    return array

def right_shift(array):
    for i in range(len(array)-1, 0, 1):
        array[i] = array[i-1]
    array[0] = None
    return None


array = [0, 1, 2, 3, 4]