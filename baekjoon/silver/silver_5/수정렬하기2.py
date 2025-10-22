#2751번
import sys
def solution():
    n = int(input())
    num = [sys.stdin.readline().strip() for _ in range(n)]

    for i in sorted(num):
        print(i)

solution()