#! /usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Solution:
    def __init__(self):
        pass

    def isPalindrome(self, x):
        return str(x)==str(x)[::-1]
        
    def calc(self,n):
        max_palindrome = 0
        for a in range(100, 1000):
            for b in range(a+1, 1000): # avoid duplicates
                prod = a*b
                if prod > max_palindrome and self.isPalindrome(prod) and n>prod:
                    max_palindrome = prod
        return max_palindrome
    
if __name__ == '__main__':
    cases = int(raw_input())
    if cases<=100:
        for i in range(cases):
            test = int(raw_input())
            s = Solution()
            print s.calc(test)