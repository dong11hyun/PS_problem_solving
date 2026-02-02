#백준 24416번
n = int(input())
count_fib1 = 1
count_fib2 = 0
def fib(n):
    if n == 1 or n == 2:
        return 1
    global count_fib1
    count_fib1 += 1  
    return fib(n - 1) + fib(n - 2)
def fib2(n):
    global count_fib2
    if n <= 2:
        return 1
    f = [0] * (n + 1)
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]
        count_fib2 += 1
    return f[i]
fib(n)
fib2(n)
print(f"{count_fib1} {count_fib2}") 


import sys

def solve():
    # 입력 속도를 높이기 위해 sys.stdin.read 사용 가능
    n = int(sys.stdin.readline())

    # 1. 재귀 함수의 'return 1' 실행 횟수 구하기
    # 이는 n번째 피보나치 수의 값과 동일함 (DP로 계산)
    fib_values = [0] * (n + 1)
    fib_values[1] = 1
    fib_values[2] = 1
    
    for i in range(3, n + 1):
        fib_values[i] = fib_values[i - 1] + fib_values[i - 2]
    
    # n번째 피보나치 수의 값
    count_fib1 = fib_values[n]
    
    # 2. 반복문의 실행 횟수
    # range(3, n + 1)은 n - 2번 반복됨
    count_fib2 = n - 2
    
    print(f"{count_fib1} {count_fib2}")

if __name__ == "__main__":
    solve()
