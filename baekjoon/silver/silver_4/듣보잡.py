import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ddd = []
bbb = []

for _ in range(n):
    ddd.append(input().strip())
for _ in range(m):
    bbb.append(input().strip())

ddd_set = set(ddd)
bbb_set = set(bbb)

answer_set = ddd_set & bbb_set
answer_list = list(answer_set)
answer_list.sort()
print(len(answer_list))
for i in answer_list:
    print(i)