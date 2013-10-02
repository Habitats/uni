#! /usr/bin/env python
# itgk oeving 3b

username = raw_input('brukernavn: ')

loggedIn = False

while loggedIn == False:
    password = raw_input('passord: ')
    if password != 'hunter2':
        print 'feil passord!'
    else:
        print 'du er naa logget inn'
        loggedIn = True
