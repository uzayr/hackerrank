# Enter your code here. Read input from STDIN. Print output to STDOUT
class Euler007:
    def __init__(self):
        pass
    
    def prime(self, num):
        max_prime = []
        d = 2
        while True:
            for i in range(2, d):
                if d%i == 0:
                    break
            else:
                max_prime.append(d)
            if len(max_prime) == num:
                return max_prime[-1]
            d+=1

if __name__ == '__main__':
    e = Euler007()
    cases = int(raw_input())
    for x in range(cases):
        test = int(raw_input())
        print e.prime(test)