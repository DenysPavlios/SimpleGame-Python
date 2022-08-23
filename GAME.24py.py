import random
randomInt = random.randint(1, 100)
print(randomInt) # for exaple
i = 1
while True:
    usertype = int(input('Take a guess number from 1 to 100  '))
    if usertype == randomInt:
        print('You WIN!!!, You the best!!!')
        print(f'You tried {i}')
        if input(f'Maybe will play again?') == 'y':
            randomInt = random.randint(1, 100)
            i = 0
        else:
            print('Thanks for game')
            break
    elif usertype < randomInt:
        print(f'You need still {randomInt - usertype} your number is less')
        print('Will try still')
        print(f'Try # {i}')
        i += 1
    else:
        print(f'You need still {usertype - randomInt} your number is more')
        print(f'Will try still')
        print(f'Try # {i}')
        i += 1
