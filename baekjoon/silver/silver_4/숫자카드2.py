import sys
input = sys.stdin.readline
from collections import Counter


ans = []

n = int(input())
user_card = list(map(int, input().split()))
m = int(input())
check_card = list(map(int, input().split()))

Answer = Counter(user_card)

for i in check_card:
    if i in user_card:
        cnt = Answer[i]
        ans.append(cnt)
    else :
        ans.append(0)

print(*ans)