'''
Created on 27. aug. 2012

@author: Habitats
'''
power = 1000;

# manual with list
listOfNum = {1, 2, 4, 8, 16}
listOfNum = (2 ** i for i in range(power))

print 'with list:'
print sum(listOfNum);

# inline example
print 'inline:'
print sum(2 ** i for i in range(power));

# locked equation
print 2 ** power - 1;
