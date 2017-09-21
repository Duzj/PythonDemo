number = 23
guess = int(input('Enter an integer:'))

if guess == number:
    print('congratulations , you guessed it')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('no , it si a little higher than that')
else:
    print('no , it is a little lower than that')

print('done')
