'''
Created on Jul 8, 2015

@author: mike
'''

from math import ceil, sqrt

def isPrime(number):
    if number == 2 or number == 3:
        return True
    elif number % 3 == 0 or number % 2 == 0:
        return False
    
    #first numbers in for loop don't work because of sqrt
    if number > pow(5, 2):
        upperBound = int(ceil(sqrt(number)))
    else:
        upperBound = number-1
        
    for i in range(2, upperBound+1):
        if number % i == 0:
            return False
        
    return True

def getPrime(num):
    currentNumber = 1
    for i in range(0, num):
        currentNumber += 1
        while not isPrime(currentNumber):
            currentNumber += 1
        print str(i) + ': ' + str(currentNumber)
        
    return currentNumber

if __name__ == "__main__":
    print getPrime(10000)