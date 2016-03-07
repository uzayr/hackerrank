#!/usr/bin/python
# Enter your code here. Read input from STDIN. Print output to STDOUT
class E:
    def __init__(self, x):
        self.num = x
        self.a = self.sumOfNumber(3)
        self.b = self.sumOfNumber(5)
        self.c = self.sumOfNumber(15)
        print self.a+self.b-self.c

    def sumOfNumber(self, num):
        a = num
        d = num
        l = self.lastNumber(num)
        n = ((l-a)/d)+1
        return (n*(a+l))/2

    def lastNumber(self, num):
        i = 0
        for a in xrange(self.num):
            if a%num == 0:
                i = a
        return i

if __name__ == '__main__':
    cases = int(raw_input())
    for i in xrange(cases):
        E(int(raw_input()))