#Task04

filein = open("/content/sample_data/input04.txt" , "r")
fileout = open("/content/sample_data/output04.txt" , "w")
x = [int(j) for j in filein.readline().strip().split(' ')]
N = x[0]
M = x[1]
print(N , M)

new_arr = []
final_arr = []
for i in range(N):
  arr =[int(i) for i in filein.readline().strip().split(' ')]
  new_arr.append(arr)
print(new_arr)

new_arr.sort(key = lambda x:x[1])
print(new_arr)
# final_arr.append(new_arr[0])
for m in range(M):
  final_arr.append(new_arr[0])
  new_arr.remove(new_arr[0])

  copy_arr = new_arr.copy()
  copy_arr.sort(key = lambda x:x[0])
  for j in range(1,len(copy_arr)):
    if copy_arr[j][0] >= final_arr[-1][-1]:
      final_arr.append(copy_arr[j])
      new_arr.remove(copy_arr[j])

print(len(final_arr))
print(final_arr)


#/////////////////////////////////////////////////////////////////////////////////////////////////////


from queue import PriorityQueue

q = PriorityQueue()


def calculate_tasks(tasks, p):
  last = [0] * p
  for i in tasks:
    q.put((i[1], i[0]))
  j = 0
  while q.qsize() > 0:
    u = q.get()
    diff = float('inf')
    diff_i = -1
    for i in range(len(last)):
      if u[1] >= last[i]:
        if (u[1] - last[i]) < diff:
          diff = u[1] - last[i]
          diff_i = i

    if diff_i != -1:
      last[diff_i] = u[0]
      j += 1

  return j


def get_tasks(input_data, output_data):
  f = open(input_data, 'r')
  f_output = open(output_data, 'w')
  n, p = [int(i) for i in f.readline().strip().split()]

  items = []
  for i in range(n):
    items.append([int(i) for i in f.readline().strip().split()])

  f_output.write(str(calculate_tasks(items, p)))


get_tasks('input04.txt', 'output04.txt')