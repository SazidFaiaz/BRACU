class myList:
    thelst = []
    # thelst.clear()
    def __init__(self, *num):
        myList.thelst.clear()
        numlst = list(num)
        myList.thelst.extend(numlst)
    def sum(self):
        print(sum(myList.thelst))
    def merge(self, *new):
        newlst = list(new)
        myList.thelst.extend(newlst)
    def average(self):
        if len(myList.thelst) == 0:
            print (f'Average: 0')
        else:
            print(sum(myList.thelst)/len(myList.thelst))

l1 =  myList(2,3,4,5,6)
l1.sum()
l1.merge(4,5,9)
l1.sum()
l1.average()
print('-----------------------------')
l2 =  myList()
l2.average()
l2.merge(1,2,4,8)
l2.sum()