
import sys

def solve():
    n = int(sys.stdin.readline())
    val1 = 1
    val2 = 2
    current = 0
    for i in range(3,n+1):
        current = (val1 + val2) % 15746
        val1 = val2
        val2 = current

    return current
print(solve())





