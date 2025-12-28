#2346
from collections import deque
import sys
input = sys.stdin.readline

def solve():
    ans = []
    n = int(input())
    data = list(map(int, input().split()))
    d = deque([(i + 1, val) for i, val in enumerate(data)])
    
    while d:
        first_key, first_val = d.popleft()
        ans.append(first_key)
        if not d:
            break

        if first_val > 0:
            for j in range(first_val-1):
                d.append(d.popleft())
        else :
            for j in range(abs(first_val)):
                d.appendleft(d.pop())
    print(*(ans))
solve()





