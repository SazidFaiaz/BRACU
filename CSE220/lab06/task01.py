#Part a
def facorial(num):
    if num == 0 or num ==1:
        return 1
    else:
        return(num * facorial(num-1))
num = 4
print("Factorial:", facorial(num))


#Part b
def fib(num):
    if num == 1 or num == 0:
        return num
    else:
        return (fib(num-1)+fib(num-2))
num = 10
print("Fibonachi", fib(num))

#part c
def printing(arr, index):
    if index == len(arr):
        return
    print(arr[index])
    printing(arr, index+1)

arr = [1,2,3,4,5]
printing(arr,0)

#part d
def basepower(base, power):
    if power == 0:
        return 1
    else:
        return base*basepower(base, power-1)

print(basepower(3,2))