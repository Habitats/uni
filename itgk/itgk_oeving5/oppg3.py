#! /usr/bin/env python
# itgk oeving 5 - oppg3

import random

def ranAns():
    ans = random.randint(1,999)
    return ans

def theGame(ans):

    tries = 10
    guess = input('guess a number between 0 and 1000\n> ')

    while guess != ans and tries > 0:
        if guess < ans:
            print 'too low!'
        else:
            print 'too much!'
        guess = input('guess another number!\n> ')
        tries -= 1
    if tries == 0:
        print 'the game, you lost!' + '\n'*3
    else:
        print 'you won yay' + '\n'*3

while True:
    theGame(ranAns())



