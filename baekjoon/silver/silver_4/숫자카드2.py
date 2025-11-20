import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
user_card = list(map(int, input().split()))
m = int(input())
check_card = list(map(int, input().split()))

Answer = Counter(user_card)
ans = []

for i in check_card:
    ans.append(Answer[i])

print(*ans)