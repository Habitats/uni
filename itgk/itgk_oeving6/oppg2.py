#! /usr/bin/env python
# itgk oeving 6 - oppg1a

def isSentence(string):
    space = ' '
    if space in string:
        return True 

def revString(string):
    revString = string[::-1]
    return revString

def palindrom(string):
    if string == revString(string):
        return True

def containsParent(string,parent):
    if string == parent:
        return 1 
    elif string in parent:
        return -1 

def childPos(string,parent):
    pos = parent.find(string,0,len(parent))
    return pos
        
# check a single string
def singleStringCheck():
    pass
    x = raw_input('enter a word or a string\n> ')

    print '"%s" reversed is "%s"' % (x,revString(x))

    if palindrom(x) == True:
        print '"%s" is a palindrom\n' % x
    if isSentence(x) == True:
        print '"%s" is a sentence\n' % x
    run()

# check two strings
def twoStringCheck():
    print 'enter two sets of strings'
    x = raw_input('1: ')
    y = raw_input('2: ')

    if containsParent(x,y) == -1:
        print '"%s" is also in "%s"; located at the position starting at: %s' % (x,y,childPos(x,y)+1)
    elif containsParent(x,y) == 1:
        print '"%s" and "%s" are identical' % (x,y)
    else:
        print '"%s" is not in "%s"' % (x,y)
    run()

# strip string
def strip(): 
    x = raw_input('enter a string you want to strip\n> ')
    stripped = 0
    for i in x: 
        if i.isalnum():
            stripped = str(stripped)+str(i) 
    print stripped.lower()[1:]
    run()

# run stuff
def run():
    print 'choose a scrip'
    z = input('1 = reverse, 2 = identical, 3 = strip\n> ')
    if z == 1:
        singleStringCheck()
    elif z == 2:
        twoStringCheck()
    elif z == 3:
        strip()
    else:
        return

run()



