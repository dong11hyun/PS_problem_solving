import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    stack = []
    for _ in range(n):
        command = input().split()
        op = command[0]

        if op == '1':
            stack.append(command[1])
        elif op == '2':
            if stack:
                print(stack.pop())
            else :
                print('-1')
        elif op == '3':
            print(len(stack))
        elif op == '4':
            if len(stack) == 0:
                print('1')
            else :
                print('0')
        elif op == '5':
            if stack:
                print(stack[-1])
            else : 
                print('-1')

solve()




