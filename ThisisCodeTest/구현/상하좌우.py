x,y = 1,1
n = 5
move = ['R','R','R','U','D','D']

for moving in move:
    if moving == 'R':
        y += 1
        if y > n :
            y -= 1
    elif moving == 'U':
        x -= 1
        if x < 1 :
            x += 1
    elif moving == 'L':
        y -= 1
        if y < 1 :
            y += 1
    else :
        x += 1
        if x > n:
            x -= 1
print(x,y)


x, y = 1, 1
n = 5
moves = ['R', 'R', 'R', 'U', 'D', 'D']

# 이동 방향 정의: R, L, U, D 순서
# dx, dy를 사용하면 x, y 좌표의 변화를 직관적으로 표현 가능
# 보통 문제 풀이에서 x는 행(세로), y는 열(가로)을 의미
dx = [0, 0, -1, 1]  # U, D에 대한 x 변화량
dy = [1, -1, 0, 0]  # R, L에 대한 y 변화량
move_types = ['R', 'L', 'U', 'D']

# 이동 계획을 하나씩 확인
for move in moves:
    # 이동 후 좌표 구하기
    nx, ny = -1, -1 # 임시 좌표 초기화
    for i in range(len(move_types)):
        if move == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    
    # 이동 수행
    x, y = nx, ny

print(x, y) # 결과: 3 4
