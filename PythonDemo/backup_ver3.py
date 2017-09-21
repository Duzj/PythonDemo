import os
import time
import zipfile
source = ['/Users/duzhijian/Desktop/crash']

target_dir = '/Users/duzhijian/Desktop/backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

comment = input("Enter a conmment -> ")

if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ','_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('successfully creater dirctory', today)

zip_command = "zip -r {0} {1}".format(target,''.join(source))

print('zip command is:')

print(zip_command)

print('running:')


f = zipfile;

#
# if os.system(zip_command) == 0:
#     print('successfully backup to',target)
# else:
#     print('backup failure')
