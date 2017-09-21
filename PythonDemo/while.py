number = 23
running = True

while running:
    guess = int(input('enter an integer :'))

    if guess == number:
        print('congratulations ,you guessed it')
        running = False
    elif guess < number:
        print('no it is a highter than that')
    else:
        print('no it is a little lower than that ')
else:
    print('the whole loop is over')

print('done')
