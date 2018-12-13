#function without parameters and without return
def div():
    mul()
    no1=10
    no2=2
    print("Div=",no1/no2)
def mul():
    sub()
    no1=10
    no2=2
    print("Mul=",no1*no2)
def sub():
    add()
    no1=10
    no2=2
    print("Sub=",no1-no2)
def add():
    no1=10
    no2=2
    print("Add=",no1+no2)
div()




