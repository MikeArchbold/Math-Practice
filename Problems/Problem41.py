'''
Created on Jul 14, 2015

@author: mike
'''
from Problems.Problem7 import isPrime

def isPandigital(number):
    numberString = str(number)
    digits = list(numberString)
    
    for digit in range(1, len(digits)+1):
        if not containsItem(digits, digit):
            return False
    
    if len(digits) == len(set(digits)):
        return True
    else:
        return False

def containsItem(myList, item):
    for currentItem in myList:
        if currentItem == str(item):
            return True
    return False
        
'''def makePandigitalNums():
    number = 321
    numList = list(number)
    for digit in numList:
        current = numList[1]
            for i 
'''
def joinNumberList(numList):
    numMap = map(str, numList)
    numMap = ''.join(numMap)
    return int(numMap)

if __name__ == '__main__':
    for i in range(0,987654321):
        print i
    '''number = 7654321
    while True:
        if isPandigital(number):
            if isPrime(number):
                break
            else:
                number -= 1
        else:
            number -= 1
        if number % 10000 == 0:
            print number
    '''
    '''if isPrime(number):
                break
        else:
            number -= 1'''
    print "correct number is " + str(number)