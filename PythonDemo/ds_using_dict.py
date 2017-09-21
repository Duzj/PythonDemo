ab = {
    'swaroop': 'swaroop@swaroopch.com',
    'larry': 'larry@wall.org',
    'matsumoto': 'matz@ruby-lang.org',
    'spammer': 'spammer@hotmail.com'
}

print('swaroop`s address is',ab['swaroop'])

del ab['spammer']

print('\n There are {} contacts in the address-bood\n'.format(len(ab)))

for [name,address] in ab.items():
    print('contact {} at {}'.format(name,address))


ab['guido'] = 'guido@python.org'

if 'guido' in ab:
    print('\n guido1 address is',ab['guido'])
