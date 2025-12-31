import sys
from math import factorial

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    try:
        n, m = map(int, line.split())
        
        result = factorial(m) // (factorial(n) * factorial(m - n))
        
        print(result)
    except ValueError:
        return

line = sys.stdin.readline()
if line:
    t = int(line.strip())
    for _ in range(t):
        solve()