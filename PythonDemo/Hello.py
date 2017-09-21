#这是注释
print("hello")

#"""""" 三引号 表示可以换行的
# print(""" dsfadsf
# dfasdfas
# fasfda""")

age = 20
name = "swap"
#使用format 来格式化输出字符串
print("{0} was {1} years old when he wrote this book".format(name,age))
print("{0} age is {1}".format(name,age))

print("{} age is {}".format(name,age))

print(name + "is" + str(age) + 'years old')

# 格式化浮点数
print('{:.3f}'.format(10.0/3))
# 一共保留几位
print('{:.3}'.format(10.0/3))

# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format("hello"))

print('{name} is {age} year old'.format(name='swap',age=20))

# 指定print尾部以空格结尾,正常会换行
print('a', end=' ')
print('b', end=' ')
print('c')

print('a', end='')
print('b', end='')
print('c')

#  加r 代表原始字符串
print(r'fasdfas\n')

i = 5
print(i)
i = i+1
print(i)

s = """this is a multi-line string .
 this is the second line."""
print(s)
