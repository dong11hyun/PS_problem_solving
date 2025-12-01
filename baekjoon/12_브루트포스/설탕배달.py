#2839번
def solution():
    n = int(input())
    result = 0
    while n >= 0:
        if n % 5 == 0:
            result +=  n // 5
            print(result)
            return
        n -= 3
        result += 1    
    print(-1)

solution()

