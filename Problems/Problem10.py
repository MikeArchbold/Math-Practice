'''
Created on Jul 10, 2015

@author: mike
'''
from Problems.Problem7 import isPrime

def sumOfAList(myList):
    summation = 0
    for i in myList:
        summation += i
    return summation

def getListOfPrimes(high):
    myList = []
    for i in range(2, high):
        if isPrime(i):
            myList.append(i)
    return sumOfAList(myList)
    
if __name__ == '__main__':
    print getListOfPrimes(2000000)