import sys
n = int(sys.stdin.readline())
result = []    
real_count = 0  
def check(current_row):
    for i in range(current_row):
        if result[i] == result[current_row] or \
           abs(result[i] - result[current_row]) == abs(i - current_row):
            return False 
    return True 
def queen(depth):
    global real_count 
    if depth == n:
        real_count += 1
        return
    for col in range(n):
        result.append(col) 
        if check(depth):
            queen(depth + 1) 
        result.pop()
queen(0)
print(real_count)




import sys

# 입력 속도 향상을 위한 설정
input = sys.stdin.readline

def solve_n_queen():
    try:
        line = input().strip()
        if not line:
            return # 입력이 없는 경우 처리
        n = int(line)
    except ValueError:
        return

    ans = 0
    
    # [최적화 핵심] 
    # 검사 속도를 O(1)로 만들기 위한 3개의 룩업 테이블
    # v1: 열 검사 (인덱스: col)
    # v2: 오른쪽 위 대각선 (/) 검사 (인덱스: row + col) -> 합은 최대 2n
    # v3: 왼쪽 위 대각선 (\) 검사 (인덱스: row - col) -> 차는 음수가 될 수 있어 n을 더해 보정 -> row - col + n
    
    v1 = [False] * n
    v2 = [False] * (2 * n)
    v3 = [False] * (2 * n)

    def dfs(row):
        nonlocal ans
        
        # Base Case: 마지막 행까지 무사히 퀸을 다 채웠다면 성공
        if row == n:
            ans += 1
            return

        # 현재 행(row)에서 0번 열부터 n-1번 열까지 시도
        for col in range(n):
            # 1. 가지치기 (Pruning): 공격 받는 위치면 무시
            if not v1[col] and not v2[row + col] and not v3[row - col + n]:
                
                # 2. 퀸 놓기 (상태 기록)
                v1[col] = True
                v2[row + col] = True
                v3[row - col + n] = True
                
                # 3. 다음 행으로 이동 (재귀)
                dfs(row + 1)
                
                # 4. 백트래킹 (상태 복구): 나와서 다른 열도 시도해봐야 하므로
                v1[col] = False
                v2[row + col] = False
                v3[row - col + n] = False

    dfs(0)
    print(ans)

if __name__ == "__main__":
    solve_n_queen()