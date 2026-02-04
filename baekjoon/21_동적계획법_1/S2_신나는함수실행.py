import sys

# 빠른 입출력을 위해 사용
input = sys.stdin.readline

# 0~20까지의 값을 저장할 3차원 배열 (Memoization Table)
# 범위가 0~20이므로 크기는 21x21x21로 설정
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def w(a, b, c):
    # Base Case 1: 하나라도 0 이하이면 1 반환
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    # Base Case 2: 하나라도 20 초과이면 w(20, 20, 20) 호출
    # 이 로직 덕분에 dp 테이블의 인덱스를 벗어나지 않게 됨
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # Memoization Check: 이미 계산된 값이 있다면 그 값을 반환
    if dp[a][b][c]:
        return dp[a][b][c]

    # Recursive Logic: 조건에 따라 점화식 수행 및 결과 저장
    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    
    return dp[a][b][c]

# 메인 실행 루프
while True:
    a, b, c = map(int, input().split())
    
    # 종료 조건
    if a == -1 and b == -1 and c == -1:
        break
    
    # 결과 출력
    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")