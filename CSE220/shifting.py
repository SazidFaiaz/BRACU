#left shift
given = [1,2,3,4,5]
for j in range(1):
    for i in range(1 , len(given)):
        given[i-1] =given[i]
    given[len(given)-1] = None
print(given)

#right shift

new = [1,2,3,4,5,]
for i in range(len(new)-1, 0, -1):
    new[i] = new[i-1]
new[0] = None
print(new)
