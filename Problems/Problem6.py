'''
Created on Jul 8, 2015

@author: mike
'''

def squareList():
    listSum = 0
    for i in range(0,101):
        listSum += pow(i, 2)
    return listSum

def addList():
    listSum = 0
    for i in range(0, 101):
        listSum += i
    return listSum

if __name__ == '__main__':
    print pow(addList(), 2) - squareList()