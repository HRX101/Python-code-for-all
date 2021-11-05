class acc:
    def __init__(self,id1,name,bal):
        self.id1=id1
        self.name=name
        self.bal=bal
    def get_name(self):
        return self.name
    def get_money(self):
        return self.bal
    def depos(self,am):
        self.bal=self.bal+am
        return self.bal
    def withdrawl(self,am):
        if am>self.bal:
            return "not enough"
        self.bal-=am
        return self.bal

ca=acc(1,"hrithik",10)
print(ca.get_money(),ca.depos(1000),ca.withdrawl(2000))
ca1=acc(2,'sayani',10)
print(ca1.get_money(),ca1.depos(2000),ca1.withdrawl(300))
print(f"lalala {ca1.id1}")
l=[ca1,ca]
for i in l:
    print(i.bal,i.name,i.id1)