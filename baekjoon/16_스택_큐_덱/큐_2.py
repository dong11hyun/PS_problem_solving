import sys
from collections import deque

input = sys.stdin.readline

def solve():
    n = int(input())
    queue = deque()
    
    for _ in range(n):
        command = input().split()
        op = command[0]
        if op == 'push':
            queue.append(command[1])
        elif op == 'pop':
            if queue:
                print(queue.popleft()) 
            else:
                print('-1')
        elif op == 'size':
            print(len(queue))
        elif op == 'empty':
            print(0 if queue else 1)
        elif op == 'front':
            if queue:
                print(queue[0])
            else:
                print('-1')
        elif op == 'back':
            if queue:
                print(queue[-1])
            else:
                print('-1')

if __name__ == "__main__":
    solve()