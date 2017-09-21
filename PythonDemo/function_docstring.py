#“函数的第一行逻辑行中的字符串是该函数的 文档字符串（DocString）”
#文档功能 函数 _doc_
def print_max(x,y):
    '''Prints the maximum of two numbers.打印两个数值中的最大数。

    The two values must be integers.这两个数都应该是整数'''
    x = int(x)
    y = int(y)

    if  x > y:
        print(x,'is maximum')
    else:
        print(y,'is maxmum')

print_max(3,6)

print(print_max.__doc__)
