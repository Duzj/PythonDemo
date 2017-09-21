import os
import time

source = ['/Users/duzhijian/Desktop/crash']

target_dir = '/Users/duzhijian/Desktop/backup'

#os.sep 根据操作系统给出相应的分隔符,
targer = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(targer,''.join(source))
# zip_command = 'zip -r {0} {1}'.format(targer,source)


print('zip command is:')
print(zip_command)
print('running:')

if os.system(zip_command) == 0:
    print('successful backup to',targer)
else:
    print('failed')
