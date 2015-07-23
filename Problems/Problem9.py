'''
Created on Jul 9, 2015

@author: mike
'''

def findPythagoreanTriple():
    MAX = 1000
    for i in range(1, MAX):
        for j in range(i+1, MAX-i):
            k = MAX - i - j
            if pow(k, 2) == pow(i, 2) + pow(j, 2):
                return i*j*k
                       
if __name__ == '__main__':
    print findPythagoreanTriple()