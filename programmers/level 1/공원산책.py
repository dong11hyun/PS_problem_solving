def solution(park, routes):
# 1. 공원 크기 및 시작 위치 찾기
    H = len(park)
    W = len(park[0])
    r, c = -1, -1
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                r, c = i, j
                break
# 2. 방향 정의
    move = {'E': (0, 1), 'W': (0, -1), 'S': (1, 0), 'N': (-1, 0)}   
# 3. 경로 순회 
    for route in routes:
        op, n_str = route.split()  # 값 나눠서 저장. op : 방향 / n_str : 거리
        n = int(n_str)
        dr, dc = move[op]
        # 이동 후 예상 위치가 아닌, 한 칸씩 이동할 경로를 검사해야 함
        temp_r, temp_c = r, c    #temp_ -> 가상위치
        is_valid_path = True
        # 4. 한 칸씩 이동하며 경로 검증
        for _ in range(n):
            nr, nc = temp_r + dr, temp_c + dc
            # 경계 검사 및 장애물 검사
            if not (0 <= nr < H and 0 <= nc < W and park[nr][nc] != 'X'):
                is_valid_path = False
                break
            temp_r, temp_c = nr, nc
        # 5. 경로가 유효할 때만 최종 위치 업데이트
        if is_valid_path:
            r, c = temp_r, temp_c
    return [r, c]