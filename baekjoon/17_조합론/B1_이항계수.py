import sys
from math import factorial
def solve():
    
    line = sys.stdin.readline()
    if not line:
        return
    n, k = map(int, line.split())
    

    result = factorial(n) // (factorial(k) * factorial(n - k))
    
    print(result)

solve()