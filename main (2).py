class account:
    def __init__(self,no,price):
        self.no=no
        self.price=price
        
    def withdrawl(self,ammount):
        if ammount>self.price:
            self.price+=ammount
        else:
            return "enough money"
class acc(account):
    def __init__(self,no,price):
        super().__init__(no,price)
        self.limit=502
    
    def show(self,ammount):
        p=super().withdrawl(self.limit)
        return p

p=acc(2,2000)
print(p.show(5020))