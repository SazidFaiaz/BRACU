
filein = open("input03.txt" , "r")
fileout = open("output03.txt" , "w")
x = int(filein.readline())
new_arr = []
final_arr = []
for i in range(x):
  arr =[int(i) for i in filein.readline().strip().split(' ')]
  new_arr.append(arr)

new_arr.sort(key = lambda x:x[1])
print(new_arr)
final_arr.append(new_arr[0])
for j in range(1,len(new_arr)):
  if new_arr[j][0] >= final_arr[-1][-1]:
    final_arr.append(new_arr[j])
print(len(final_arr))
fileout.write(f"{str(len(final_arr))}\n")
print(final_arr)
for i in range(len(final_arr)):
  fileout.write(f"{str(final_arr[i][0])} {str(final_arr[i][1])}\n")