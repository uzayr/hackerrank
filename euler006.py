#! /usr/bin/env python
# Enter your code here. Read input from STDIN. Print output to STDOUT
class Parent:
    """Parent class for OOPS"""
    def __init__(self):
        pass

    def sum(self, num):
        pass

    def sqr(self, num):
        pass

    def diff(self, a, b):
        pass

class Euler006(Parent):
    def __init__(self):
        pass

    def sum(self, num):
        return (num*(num+1)/2)**2

    def sqr(self, num):
        return num*(num+1)*(2*num+1)/6

    def diff(self, num):
        a = self.sqr(num)
        b = self.sum(num)
        return b-a

if __name__ == '__main__':
    e = Euler006()
    cases = int(raw_input())
    for i in range(cases):
        test = int(raw_input())
        print e.diff(test)