import sys
input = sys.stdin.readline
def solve():
    n = int(input())
    input().rstrip() 
    ans_set = set()
    total_gomgom = 0
    for _ in range(n - 1):
        chat = input().rstrip()
        if chat == 'ENTER':
            total_gomgom += len(ans_set)
            ans_set.clear()
        else:
            ans_set.add(chat)
    total_gomgom += len(ans_set)
    print(total_gomgom)

solve()