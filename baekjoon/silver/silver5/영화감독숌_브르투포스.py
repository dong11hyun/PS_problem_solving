# 1436번
# 브르투 포스 - 가능한 모든것을 시도해보는 알고리즘.!
import sys
def solve():
    n = int(sys.stdin.readline())
    count = 0  # N번째인지 세는 카운터
    num = 665   # 666부터 검사하기 위해 665로 시작
    while True:
        num += 1
        if "666" in str(num):
            # 2. 포함되어 있다면 카운트 증가
            count += 1
        
        if count == n:
            print(num)
            break

solve()
