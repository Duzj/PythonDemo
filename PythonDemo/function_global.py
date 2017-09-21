x = 50
#使用 global 声明这个变量是全局变量, 给全局变量赋值,改变
def fun():
    global x
    print('x is',x)

    x = 2
    print('change global x to',x)

fun()

print('value of x is ',x)
