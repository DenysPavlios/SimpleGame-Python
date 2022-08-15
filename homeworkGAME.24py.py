import random


chislo = random.randint(1, 100)
print(chislo)
i = 1
while True:
    usertype = int(input('call a number from 1 to 100  '))

    if usertype == chislo:
        print('You WIN!!!')
        print(f'You made {i} poputok')
        break
    elif usertype < chislo:
        print(f'You need still {chislo - usertype} you int smoll')
        print('poprobuy ewe')
        print(f'poputka # {i}')
        i += 1


    elif usertype > chislo:
        print(f'You need still {usertype - chislo} you int more')
        print(f'poprobuy ewe')
        print(f'poputka # {i}')
        i += 1
