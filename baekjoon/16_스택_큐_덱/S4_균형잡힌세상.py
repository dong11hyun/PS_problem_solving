import sys
def solve():
    while True:
        data = sys.stdin.readline().rstrip()
        if data == '.':
            break
        stack = []
        is_valid = True
        for i in data:
            if i == '(' or i == '[':
                stack.append(i)
            elif i == ')':
                if not stack or stack[-1] != '(':
                    is_valid = False
                    break
                stack.pop()
            elif i == ']':
                if not stack or stack[-1] != '[':
                    is_valid = False
                    break
                stack.pop()
        
        if is_valid == True and not stack:
            print("YES")
        else:
            print("NO")
solve()
