import string
import builtins
import re


def reverse(text):
    # :: 表示整个序列 -1 表示 倒序
    return text[::-1]


def is_palindrome(text):
    return text == formatter(reverse(text))


#忽略 空格 ,大小写和标点
def formatter(text):
    # out = text.translate(string.maketrans("",""), string.punctuation)
    # trantab = str.maketrans(None, string.punctuation) # 制作翻译表
    # l = text.translate(trantab)
    s = re.sub(r'[^ws]','',text)
    return s.lower()


something = input("Enter text:")

if is_palindrome(something):
    print("yes, it is apalindrome")
else:
    print("no , it is not a palindrome")
