def func(N, S, arr):
    for i in range(N):
        for j in range(i+1, N):
            if arr[i] + arr[j] == S:
                return i+1, j+1
    return "IMPOSSIBLE"

with open('input01.txt', 'r') as file:
    N, S = map(int, file.readline().split())
    arr = list(map(int, file.readline().split()))

with open('output01.txt', 'w') as file:
    idx = func(N, S, arr)
    if idx == "IMPOSSIBLE":
        file.write("IMPOSSIBLE")
    else:
        file.write(f"{idx[0]} {idx[1]}")


#02

with open('input01.txt', 'r') as file:
    N, S = map(int, file.readline().split())
    arr = list(map(int, file.readline().split()))

def func(N, S, nums):
    listt = []
    i = 0
    j = len(nums)-1
    while i<j:
      if nums[i]+nums[j] < S:
        i += 1
      elif nums[i]+nums[j] > S:
        j -= 1
      elif nums[i]+nums[j] == S:
        file.write(f"{i+1} {j+1}")
        break
with open('output01.txt', 'w') as file:
    idx = func(N, S, arr)
    if idx == "IMPOSSIBLE":
        file.write("IMPOSSIBLE")
#     # else:
#     #     file.write(f"{idx[0]} {idx[1]}")