#!/usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution:
    def __init__(self):
        pass
    
    def largestPrimeFactor(self, num):
        d = 2
        factors = []
        while d*d<=num:
            while num%d==0:
                factors.append(d)
                num//=d
            d+=1
        if num>1:
            factors.append(num)
        return max(factors)
    
if __name__ == '__main__':
    s = Solution()
    cases = int(raw_input())
    for case in range(cases):
        test = int(raw_input())
        print s.largestPrimeFactor(test)