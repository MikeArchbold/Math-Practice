'''
Created on Jul 2, 2015

@author: mike
'''
    
def divisibleBy(num, ceil):
    currentMultiple = 1
    multiples = []
    while( currentMultiple*num < ceil ):
        multiples.append( currentMultiple*num )
        currentMultiple += 1
    return multiples
    
if __name__ == '__main__':
    uniqueNums = set(divisibleBy(3, 1000) + divisibleBy(5, 1000))
    print sum(uniqueNums)