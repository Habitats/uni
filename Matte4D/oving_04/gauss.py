'''
Created on 16. sep. 2012

@author: Habitats
'''

from numpy import zeros, array
from numpy.linalg import linalg

a = array([[5, 4, 1, 6.8], [10, 9, 4, 17.6], [10, 13, 15, 38.4]], dtype=float)

def gaussElim(a):
    n = len(a) - 1
    x = [0 for i in range(n+1)]
    tmp = zeros((n + 1, n + 2))
    
    for k in range(n):
        m = k
        for j in range(k + 1, n + 1):
            if abs(a[m][k]) < abs(a[j][k]):
                m = j
                
        if a[m][k] == 0:
            print "no unique solution"
            
        else:
            a[m][k], a[k][m] = a[k][m], a[m][k]
        
        if a[n][n] == 0:
            print "no unique solution #2"
        
        else:
            for j in range(k + 1, n + 1):
                tmp[j][k] = a[j][k] / a[k][k]
                
                for p in range(k + 1, n + 2):
                    a[j][p] = a[j][p] - (tmp[j][k] * a[k][p])
                        
    print a
    print tmp
    x[n] = a[n][n + 1] / a[n][n]
    
    for i in range(n-1,0-1,-1):
        tot = 0
        for m in range(i+1,n+1):
            tot += a[i][m]*x[m]
            
        x[i] = 1/a[i][i]*(a[i][n+1]-tot)
    
    return x
    
print gaussElim(a)

a = array([[5,4,1],[10,9,4],[10,13,15]], dtype = float)
b = [6.8,17.6,38.4]
print linalg.solve(a,b)


