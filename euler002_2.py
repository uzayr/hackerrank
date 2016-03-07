#! /usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution:
    def __init__(self, test):
        self.test = test
        print self.result(test)
        
    def fib(self, x):
        a, b = 0, 1
        for i in xrange(x):
            a, b = b, a+b
        return b
        
    def result(self, x):
        out = 0
        for i in xrange(x):
            z = self.fib(i)
            if z>self.test:
                return out
            if z%2==0:
                out+=z
        return out
                
if __name__ == '__main__':
    cases = int(raw_input())
    for i in xrange(cases):
        test = int(raw_input())
        Solution(test)