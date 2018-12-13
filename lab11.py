def fun(*values):
    print(values)
    print(type(values))

#fun(10,98.35)TypeError: fun() takes 1 positional argument but 2 were given
fun(10)
fun("ravi")
fun(98.35)
fun(10,"ravi")
