import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer_set = set()
check_list = []
answer = 0

for _ in range(n):
    string = input().strip()
    answer_set.add(string)
for _ in range(m):
    string1 = input().strip()
    check_list.append(string1)

for i in check_list:
    if i in answer_set:
        answer += 1

print(answer)