def solution(n, m, section):
   
    count = 0  # 롤러질 횟수
    painted_until = 0  # 페인트가 칠해진 마지막 구역
    
    for s in section:
        if s > painted_until:
            count += 1
            painted_until = s + m - 1
    return count

n = 8
m = 4
section = [2, 3, 6]
print(f"최소 롤러질 횟수: {solution(n, m, section)}") # 예상 결과: 2

    