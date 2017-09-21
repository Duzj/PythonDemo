x = 50
#变量的作用域
def fun(x):
    print('x is',x)

    x = 2
    print('change local x to',x)


fun(x)
print('x is still',x)
