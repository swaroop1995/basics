def employee(idno=0,name=None,salary=0.0):
    print("employee id=",idno)
    print("employee name=",name)
    print("employee salary=",salary)

employee()
print("----------")
employee(102)
print("----------")
employee(name="ravi")
print("----------")
employee(salary=123000.0)