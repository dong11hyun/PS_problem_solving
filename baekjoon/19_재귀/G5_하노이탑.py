def hanoi(n, start, end, via):
    if n == 1:
        print(start, end)
        return
    
    # 1. n-1개를 시작 -> 보조 기둥으로
    hanoi(n-1, start, via, end)
    
    # 2. 가장 큰 원판을 시작 -> 목표 기둥으로
    print(start, end)
    
    # 3. n-1개를 보조 -> 목표 기둥으로
    hanoi(n-1, via, end, start)

n = int(input())
print(2**n - 1)  # 이동 횟수
hanoi(n, 1, 3, 2)
