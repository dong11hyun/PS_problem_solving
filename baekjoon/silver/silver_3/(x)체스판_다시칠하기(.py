#1018번 브루트포스
import sys
def solve():
    n, m = map(int, sys.stdin.readline().split())
    board = [sys.stdin.readline().strip() for _ in range(n)]
    min_repaint = 64  # 8x8 체스판의 최대 칠하기 횟수는 64
    # 1. 8x8 체스판을 잘라낼 시작점을 순회
    for start_y in range(n - 7):
        for start_x in range(m - 7):
            # 2. 현재 8x8 영역에 대한 두 가지 경우의 칠하기 횟수를 계산
            repaint_case_w = 0  # 'W'로 시작하는 체스판 기준
            repaint_case_b = 0  # 'B'로 시작하는 체스판 기준
            for y in range(start_y, start_y + 8):
                for x in range(start_x, start_x + 8):
                    if (y + x) % 2 == 0: #시작점 짝수
                        # 'W'로 시작하는 정답 체스판이라면 이 칸은 'W'여야 함
                        if board[y][x] != 'W':
                            repaint_case_w += 1
                        # 'B'로 시작하는 정답 체스판이라면 이 칸은 'B'여야 함
                        if board[y][x] != 'B':
                            repaint_case_b += 1
                    else: #시작점 홀수
                        # 'W'로 시작하는 정답 체스판이라면 이 칸은 'B'여야 함
                        if board[y][x] != 'B':
                            repaint_case_w += 1
                        # 'B'로 시작하는 정답 체스판이라면 이 칸은 'W'여야 함
                        if board[y][x] != 'W':
                            repaint_case_b += 1
            # 3. 두 경우 중 더 작은 값을 현재까지의 전체 최솟값과 비교하여 갱신
            current_min = min(repaint_case_w, repaint_case_b)
            min_repaint = min(min_repaint, current_min)
            
    print(min_repaint)

solve()