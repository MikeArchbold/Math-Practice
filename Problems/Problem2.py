'''
Created on Jul 2, 2015

@author: mike
'''

def fib(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return fib(num-1) + fib(num-2)

def getEvens():
    fibNumber = 2
    total = 0
    x = 2
    while fibNumber < 4000000:
        if fibNumber % 2 == 0:
            total += fibNumber
        x += 1
        fibNumber = fib(x)
    return total
            
if __name__ == '__main__':
    print getEvens()