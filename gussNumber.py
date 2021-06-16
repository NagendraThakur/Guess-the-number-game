import random
import math



try:
    min = int(input('Enter min range:- '))
    max = int(input('Enter max range:- '))
    count = 0
    x = random.randint(min, max)
    times = round(math.log(max - min + 1, 2))
    print('\n\t\tYou have only ', times,'changes')
except:
    print ('Invalid ranges have been entered.\nThus the program is being terminated.')
else:
    while count < times:
        count += 1
        guess = int(input('Guess a number:- '))

        if x == guess:
            print('Congratulations you did it in ',
                  count, ' try')
            break
        elif x > guess:
            print('You guessed too small!')
        else:
            print('You Guessed too high!')
    if count >= times:
        print('\n\tThe guess number is %d' % x)
finally:
    print ('\t\tThank You\n\tFor Playing the Game')



 

