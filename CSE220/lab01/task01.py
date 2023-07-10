import fhm_unittest as unittest
import numpy as np
def playRight(sequence, beats):
    for i in beats:
        if i ==1:
            temp = sequence[0]
            for j in range(len(sequence)-1 , -1 , -1):
                sequence[(i + 1) % len(sequence)] = sequence[i]
            sequence[1] = temp
    return sequence

print("///  Test 01: Play Right  ///")
sequence=np.array([10,20,30,40,50,60])
beats = np.array([1,0,0,1,0,1])
returned_value = playRight(sequence, beats)
print(f'Task 1: {returned_value}') # This should print [40, 50, 60, 10, 20, 30]
unittest.output_test(returned_value, np.array([40, 50, 60, 10, 20, 30]))