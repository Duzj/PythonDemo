# encoding=utf-8


class ShortInputException(Exception):

    def __init__(self, length , ateast):
        Exception.__init__(self)
        self.legth = length
        self.ateast = ateast


try:
    text = input("Enter soming ->:")
    if len(text) < 3 :
        raise ShortInputException(len(text),3)
except EOFError:
    print("发的撒")
except ShortInputException as ex:
    print(ex.legth,ex.ateast)
else:
    print("no  yes")

