#20920
import sys
input = sys.stdin.readline
from collections import Counter

n ,m = map(int, input().split())

word_all = []

for i in range(n):
    word = input().rstrip()
    if len(word) >= m:
        word_all.append(word)

c = Counter(word_all)
result = list(c.keys())

# 3순위부터 역순으로 정렬 (안정 정렬 활용)
result.sort()                          # 3순위: 사전순 오름차순
result.sort(key=lambda x: len(x), reverse=True)   # 2순위: 길이 내림차순
result.sort(key=lambda x: c[x], reverse=True)     # 1순위: 빈도수 내림차순

#result = sorted(c.keys(), key=lambda x: (-c[x], -len(x), x))
for word in result:
    print(word)

