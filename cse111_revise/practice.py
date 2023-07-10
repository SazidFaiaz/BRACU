import fhm_unittest as unittest
import numpy as np
def discard(arr, idx):
    for i in range(idx, len(arr)-1):
        arr[i] = arr[i+1]
        arr[i+1] = None


def discardCards(arr, elem):
    while elem in arr:
        for i in range(len(arr)):
            if arr[i] == elem:
                discard(arr, i)
    return arr

print("///  Test 02: Discard Cards  ///")
cards = np.array([1,2,3,2,8,2,2,5,7])
returned_value = discardCards(cards, 2)
print(f'Task 2: {returned_value}') # This should print [1, 3, 8, 5, 7, None, None, None, None]
unittest.output_test(returned_value, [1, 3, 8, 5, 7, None, None, None, None])