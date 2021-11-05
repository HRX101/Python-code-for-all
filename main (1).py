class acc:
    def __init__(self,id1,name,bal):
        self.__id1=id1
        self.__name=name
        self.__bal=bal
    def get_name(self):
        return self.__name
    def get_money(self):
        return self.__bal
    def depos(self,am):
        self.__bal=self.__bal+am
        return self.__bal
    def withdrawl(self,am):
        if am>self.__bal:
            return "not enough"
        self.__bal-=am
        return self.__bal

ca=acc(1,"hrithik",10)
print(ca.get_money(),ca.depos(1000),ca.withdrawl(200))
ca1=acc(2,'sayani',10)
print(ca1.get_money(),ca1.depos(2000),ca1.withdrawl(300))
print(f"lalala {ca1.__dict__}")
'''
l=[ca1,ca]
for i in l:
    print(i.bal,i.name,i.id1)
'''