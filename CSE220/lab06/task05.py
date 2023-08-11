class FinalQ:

    def printt(self, array, idx):
        if idx < len(array):
            profit = self.calcProfit(array[idx])
            print("{}. Investment: {}; Profit: {}".format(idx + 1, array[idx], self.calcProfit(array[idx])))
            self.printt(array, idx + 1)

    def calcProfit(self, investmentt):
        if investmentt == 25000:
            return 0.0
        else:
            if investmentt <= 100000:
                return self.calcProfit(investmentt - 1000) + 45.0
            else:
                return self.calcProfit(investmentt - 1000) + 80.0

array = [25000, 100000, 250000, 350000]
f = FinalQ()
f.printt(array, 0)
