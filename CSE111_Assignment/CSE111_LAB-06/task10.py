class SultansDine:
    num_of_branches = 0
    total_sell = 0
    output = []

    def __init__(self, location):
        self.location = location
        SultansDine.num_of_branches += 1
        SultansDine.output.append(self)

    def sellQuantity(self, quantity):
        if quantity < 10:
            self.branch_sell = quantity * 300
        elif quantity >= 10 and quantity < 20:
            self.branch_sell = quantity * 350
        else:
            self.branch_sell = quantity * 400
        SultansDine.total_sell += self.branch_sell

    def branchInformation(self):
        x = (f"Branch Name: {self.location}\nBranch Sell: {self.branch_sell}")
        print(x)

    @classmethod
    def details(cls):
        print(f"Total Number of branch(s): {SultansDine.num_of_branches}\nTotal Sell: {SultansDine.total_sell} Taka")
        for i in SultansDine.output:
            print(f"Branch Name: {i.location}, Branch Sell: {i.branch_sell} Taka")
            i.percentage = (i.branch_sell / SultansDine.total_sell) * 100
            print("Branch consists of total sell's:", str("{:.2f}".format(i.percentage)) + "%")


SultansDine.details()
print('########################')
dhanmodi = SultansDine('Dhanmondi')
dhanmodi.sellQuantity(25)
dhanmodi.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
baily_road = SultansDine('Baily Road')
baily_road.sellQuantity(15)
baily_road.branchInformation()
print('-----------------------------------------')
SultansDine.details()
print('========================')
gulshan = SultansDine('Gulshan')
gulshan.sellQuantity(9)
gulshan.branchInformation()
print('-----------------------------------------')
SultansDine.details()