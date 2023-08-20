#Task01:
fileIn = open("task01_Input.txt", mode='r')
outputFile = open('task01_Output.txt', mode='w')

num = fileIn.readline()
newlist = fileIn.readlines()
print(newlist)
print(newlist[0])

for line in newlist:
  stripline = line.strip('\n')
  print(stripline)

  if int(stripline)%2 == 0:
    print(f"{stripline} is even")
    outputFile.write(f"{stripline} is even \n")
  else:
    print(f"{stripline} is odd")
    outputFile.write(f"{stripline} is odd \n")


#Task02:

fileIn = open("task02_input.txt", mode='r')
outputFile = open('task02_output.txt', mode='w')
x = fileIn.readline()
for i in range(int(x)):
  y = fileIn.readline()
  splitY = y.split(' ')
  # print(y)
  print(splitY)
  # stripline = splitY[3].strip('\n')
  # print(stripline)

  if splitY[2] == "+":
    sum = int(splitY[1]) + int(splitY[3].strip('\n'))
    print(sum)
    outputFile.write(f"The result of {splitY[1]} + {int(splitY[3])} is {sum}\n")
  elif splitY[2] == "/":
    div = int(splitY[1]) // int(splitY[3].strip('\n'))
    print(div)
    outputFile.write(f"The result of {splitY[1]} / {int(splitY[3])} is {div}\n")
  elif splitY[2] == "*":
    mul = int(splitY[1]) * int(splitY[3].strip('\n'))
    print(mul)
    outputFile.write(f"The result of {splitY[1]} * {int(splitY[3])} is {mul}\n")
  else:
    sub = int(splitY[1]) - int(splitY[3].strip('\n'))
    print(sub)
    outputFile.write(f"The result of {splitY[1]} - {int(splitY[3])} is {sub}\n")

#Task03:

# fileIn = open("Input1Task03.txt", mode='r')
# outputFile = open('output01task03.txt', mode='w')
# elem = fileIn.readline()
# allem = fileIn.readlines()
# print(allem)