class FinalQ:

    def printt(self, array, idx):
        if idx < len(array):
            profit = self.calprofit(array[idx])
            print(f"profit for investment: {array[idx]} and calculated profit: {profit} USD")
            self.printt(array, idx + 1)

    def calprofit(self, investmentt):
        if investmentt == 20000:
            return 0.0
        else:
            if investmentt <= 100000:
                return self.calprofit(investmentt - 1000) + 45.0
            else:
                return self.calprofit(investmentt - 1000) + 80.0


array = [25000, 100000, 250000, 350000]
FinalQ().printt(array, 0)