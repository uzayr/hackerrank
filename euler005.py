#!/usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Euler005:
    def __init__(self):
        pass
    
    def calc(self,num):
        lcm = 1
        for i in range(num):
            a = lcm
            b = i+1
            lcm = a*b/self.gcd(a,b)
        return lcm
    
    def gcd(self, b, a):
        while(b!=0):
            t = b
            b = a%b
            a = t
        return a
    
if __name__ == '__main__':
    e = Euler005()
    cases = int(raw_input())
    for i in range(cases):
        test = int(raw_input())
        print e.calc(test)