from multipledispatch import dispatch

class calculator:

    @dispatch(int , int)
    def product(self , a , b ):
        print(a*b)
    

    @dispatch(int , int  , int)
    def product(self , a  , b , c ):
        print(a*b*c)

    @dispatch(str , int)
    def product(self , a , b):
        print(int(a)*b)
    


 

c1 = calculator()
# c1.product(10)
c1.product(10 , 5)
c1.product(20 , 10 , 4)
c1.product('10' , 2)