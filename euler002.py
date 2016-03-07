#!/usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution:
    def __init__(self, test):
        self.test = test
        print self.result(test)
        
    def fib(self, x):
        if x==0: return 0
        elif x==1: return 1
        else: return self.fib(x-1) + self.fib(x-2)
        
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