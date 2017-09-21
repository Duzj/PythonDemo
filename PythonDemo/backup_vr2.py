import os
import time

source = ['/Users/duzhijian/Desktop/crash']

target_dir = '/Users/duzhijian/Desktop/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

target = today + os.sep + now + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('successfully created dirctory',today)

zip_command = 'zip -r {} {}'.format(target,''.join(source))

print('zip command is:')

print(zip_command)

print('running:')

if os.system(zip_command) == 0 :
    print('successfully backup to',target)
else:
    print('failure')
