'''
Created on 29. aug. 2012

@author: Habitats
'''
from timeit import timeit, Timer

class MyClass:
    ans = 1
    
    # assigns an /own/ ans if instantiated like "cls = MyClass()", not accessible by "MyClass.ans" (kinda like /static/)
    def __init__(self):
        self.ans = 0
    
    def addition(self, x, y):
        return x + y
    def multiply(self, x, y):
        return x * y
    
    def multiplyThenAdd(self, x, y):
        ans = self.multiply(x, y)
        ans += self.addition(x, y)
        return ans
        


#cls = MyClass()
#print MyClass.ans
#print cls.ans
#print MyClass.ans == cls.ans
#
#print cls.multiplyThenAdd(2, 2)

class Recursion:
    def __init__(self):
        self.counter = 0
    
    def s(self, seq, i=0):
        if i == len(seq):
            return 0
        ans = self.s(seq , i + 1) + 1
        return ans
    
rec = Recursion()

derp = range(1, 990)

print rec.s(derp)
