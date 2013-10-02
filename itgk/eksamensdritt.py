#! /usr/bin/env python

def mystery(n,x):
    res = 0
    if n>0:
        res = x*mystery(n-1,x)
                
    else:
        res = 1

    return res

print mystery(3,2)
