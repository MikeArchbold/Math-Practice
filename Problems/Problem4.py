'''
Created on Jul 7, 2015

@author: mike
'''

def palindrome():
    largest = 0, 0, 0
    for i in reversed(range(100, 1000)):
        for j in range(100,1000):
            original = str(i*j)
            if original == original[::-1] and i*j > largest[0]:
                largest = i*j, i, j
    return largest
        
if __name__ == '__main__':
    print palindrome()