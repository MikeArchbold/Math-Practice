'''
Created on Jul 13, 2015

@author: mike
'''
from Problems.Problem7 import isPrime
import unittest

class Test(unittest.TestCase):
    
    def test(self):
        allPowers = []
        for i in range(2,101):
            allPowers = allPowers + list(set(self.powersOfSequence(i)) - set(allPowers))
        print len(allPowers)
        
    if __name__ == '__main__':
        unittest.main()
        
    def createPrimeNumbersList(self, totalNumbers):
        listOfPrimes = []
        primeNumber = 2
        for i in range(0,totalNumbers):
            while not isPrime(primeNumber):
                primeNumber += 1
            listOfPrimes.insert(i, primeNumber)
            primeNumber += 1
        return listOfPrimes

    def powersOfSequence(self, base):
        listOfPowers = []
        for i in range(2,101):
            listOfPowers.append(pow(base, i))
        return listOfPowers

    #if __name__ == '__main__':
    '''allPowers = []
    for i in range(2,101):
        allPowers = allPowers + list(set(powersOfSequence(i)) - set(allPowers))
    print len(allPowers)'''