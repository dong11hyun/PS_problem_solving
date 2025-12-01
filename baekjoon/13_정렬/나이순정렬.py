import sys
input = sys.stdin.readline

n = int(input())
members = []

for _ in range(n):
    age, name = input().split()
    members.append((int(age), name))

#안정정렬 -> 나이만 해도 입력순서 보장해서, 알아서정렬
members.sort(key=lambda x: x[0])

for age, name in members:
    print(age, name)