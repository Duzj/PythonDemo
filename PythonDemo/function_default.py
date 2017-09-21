def say(message,times=1):
    print(message * times)

say('hello')

say('world ', 5)


def fun(a,b=5,c=10):
    print('a is',a, 'and b is',b ,'and c is',c)

fun(3,6)

fun(25,c=23)

fun(c=40,a=20,b=10)

