import sys
import os
import os
print('The conmand line arguments are:')

for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is',sys.path,'\n')

print(os.getcwd())
