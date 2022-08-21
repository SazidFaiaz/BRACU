
class calculator:

    # def sum(self , num1 , num2=None , num3 = None ):
    #     if num1 != None and num2 != None and num3 != None:

    #         print(num1 + num2 + num3)
    #     elif num1 != None and num2 != None :
    #         print(num1 + num2)
    #     else:
    #         print(1*num1)
    def sum(self , *nums):
        sum = 0
        for i in nums:
            sum = sum + i
        print(sum)

c1 = calculator()
c1.sum(10)
c1.sum(10 , 5)
c1.sum(20 , 10 , 4)
c1.sum(1,2,3,4,5,6,7,8,9,10)