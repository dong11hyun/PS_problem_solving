import sys
input = sys.stdin.readline

n = int(input())
check_set = set()
for i in range(n):
    n, m = input().split()
    if n == 'ChongChong' or m == 'ChongChong':
        check_set.add(n)
        check_set.add(m)
    elif n in check_set or m in check_set:
        check_set.add(n)
        check_set.add(m)
    else:
        continue
print(len(check_set))