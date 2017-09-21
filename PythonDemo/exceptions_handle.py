
try:
    text = input('Enter someing ->:')
except EOFError:
    print("why didi you do an eof on me?")
except KeyboardInterrupt:
    print("you cacelled the operation")
else:
    print("you entered {}".format(text))
