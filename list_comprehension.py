# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
X, Y, Z, N = map(int, sys.stdin)
arr = [[X, Y, Z] for X in range(X+1) for Y in range(Y+1) for Z in range(Z+1) if X + Y + Z != N]
print arr
