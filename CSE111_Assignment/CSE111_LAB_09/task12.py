
class AppleProduct:
  def __init__(self, name, model, base_price):
    self.name = name
    self.model = model
    self.base_price = base_price
  def companyInfo(self):
    st = ("Company Name: Apple\nFouder: Steve Jobs, Steve Wozniak, Ronald Wayne"
          "\nCurrent CEO: Tim Cook\nAddress: Apple Inc, 2511 Laguna Blvd, Elk Grove,"
          " CA 95758, United States")
    return st
  def feature(self):
    st = (f"Name: {self.name}\nProduct Model: {self.model}\nHardware "
          "Quality: Excellent Hardwares\nGuarantee/ Warranty: Apple Care")
    return st
  def __str__(self):
    print('This is apple product.')
  def calculatePrice(self):
    print('Total Price:', self.base_price)
  # def __add__(self, other):
  #   self.totalprice + other.totalprice

class MacBookPro2020(AppleProduct):
  def __init__(self, name, model, ram, chip, tax):
    super().__init__(name, model, 1299)
    self.ram = ram
    self.chip = chip
    self.tax = tax
    self.totalprice = 0
  def __str__(self):
    return (f' Product Details:\nName: {self.name}\nProduct model: {self.model}\nHardware Quality: Excellent Hardwares'
            f'Guarantee/ Warranty: Apple Care \nRam: {self.ram}\nchip: {self.chip} Company Details:\n{super().companyInfo()}'
            )
  def calculatePrice(self):
    self.totaltax = (self.base_price * self.tax)/100
    self.totalprice = self.totaltax + self.base_price
    print(f'Calculating Total Price:\nBase Price: {self.base_price}'
          f'\nTax: {self.tax}%\nTotal Price: {self.totalprice}')

class iPhone12(AppleProduct):
  def __init__(self, name, model, ram, chip, tax):
    super().__init__(name, model, 799)
    self.ram = ram
    self.chip = chip
    self.tax = tax
    self.totalprice = 0
  def __str__(self):
    return (f' Product Details:\nName: {self.name}\nProduct model: {self.model}\nHardware Quality: Excellent Hardwares'
            f'Guarantee/ Warranty: Apple Care \nRam: {self.ram}\nchip: {self.chip} Company Details:\n{super().companyInfo()}'
            )
  def calculatePrice(self):
    self.totaltax = (self.base_price * self.tax)/100
    self.totalprice = self.totaltax + self.base_price
    print(f'Calculating Total Price:\nBase Price: {self.base_price}'
          f'\nTax: {self.tax}%\nTotal Price: {self.totalprice}')


m1 = MacBookPro2020('MacBook', 'MacBookPro2020', 8, 'M1', 10)
print(m1)
print('====================================')
m1.calculatePrice()
print('###################################')
iphone = iPhone12('iPhone', 'iPhone 12', 8, 'A14', 5)
print(iphone)
print('====================================')
iphone.calculatePrice()
print('###################################')
print('Total Price of these two products: ', end='')
# print('%.2f Dollars'%(m1 + iphone))