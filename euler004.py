#!/usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution:
    def __init__(self, test):
        self.test = test
        print self.iterate()
    
    def isPalindrome(self, x):
        if str(x)==str(x)[::-1]:
            return True
        else:
            return False
        
    def iterate(self):
        result = []
        for x in xrange(100,1000):
            for y in xrange(100,1000):
                check = x*y
                if self.isPalindrome(check) and check<self.test:
                    result.append(check)
        return max(result)
        
if __name__ == '__main__':
    cases = int(raw_input())
    for i in xrange(cases):
        test = int(raw_input())
        Solution(test)