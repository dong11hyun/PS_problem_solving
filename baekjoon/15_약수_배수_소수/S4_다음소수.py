import sys
input = sys.stdin.readline

#약수 구하는 방법 - 그 수의 루트값까지만 나눠보면 충분함. 더 할 필요 없음.
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def solution(n):
    while True:
        if is_prime(n):
            print(n)
            break
        n += 1

N = int(input())
check = []
ans =[]
for _ in range(N):
    check.append(int(input()))
for _ in check:
    ans.append(solution(_))
