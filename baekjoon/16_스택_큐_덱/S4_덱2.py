# 28279
import sys
from collections import deque
input = sys.stdin.readline
def solve():
    n = int(input())
    deck = deque()
    for _ in range(n):
        command = input().split()
        op = command[0]

        if op == '1':
            deck.appendleft(command[1])
        elif op == '2':
            deck.append(command[1])
        elif op == '3':
            if deck:
                print(deck.popleft())
            else : 
                print('-1')
        elif op == '4':
            if deck:
                print(deck.pop())
            else :
                print('-1')
        elif op == '5':
            print(len(deck))
        elif op == '6':
            if deck:
                print('0')
            else :
                print('1')
        elif op == '7':
            if deck:
                print(deck[0])
            else :
                 print('-1')
        elif op == '8':
            if deck :
                print(deck[-1])
            else :
                print('-1')

solve()
