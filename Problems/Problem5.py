'''
Created on Jul 7, 2015

@author: mike
'''

def canBeDivided():
    dividend = 20
    lower = 2
    upper = 10
    
    while True:
        for i in range(lower, upper+1):
            if dividend % i > 0:
                break
            elif i == upper:
                return dividend
        dividend += 1
        
def fib(n):
    a, b = 0, 1
    while a<n:
        print a,
        a, b = b, a+b
              
if __name__ == '__main__':
    print fib(10)