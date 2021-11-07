def deco(func):
    def new(val,val1):
        if(type(val)==type(val1)):
            return func(val,val1)
        else:
            return func(str(val),str(val1))
    return new


@deco
def concat(val,val1):
    return val+val1
    
print(concat("hrithik","paul"))
print(concat(12,"hi"))