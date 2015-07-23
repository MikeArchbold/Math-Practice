'''
Created on Jul 7, 2015

@author: mike
'''

import math
from math import ceil

def isPrime(num):
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    
    for i in range(3, int(ceil(math.sqrt(num))), 2):
        if num % i == 0:
            print str(num) + ' % ' + str(i) + ' = 0'
            return False
    return True
    
def largestPrime(num):
    i = 2
    if num % i == 0:
        return num / i
    
    i += 1 
    holdLower = 0
    while i < int(ceil(math.sqrt(num))):
        if num % i == 0:
            if isPrime(num / i):
                return num / i
            elif isPrime(i):
                holdLower = i
        i += 2
    return holdLower

if __name__ == "__main__":
    print largestPrime(600851475143)