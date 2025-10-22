import sys
input = sys.stdin.readline
def solve():
    paper = [[0] * 100 for _ in range(100)]
    n = int(input())
    for _ in range(n):
        x,y = map(int, input().split())
        for i in range(x,x+10):
            for j in range(y,y+10):
                paper[i][j] = 1
    black_area = 0
    for row in paper:
        black_area += sum(row)
    print(black_area)
    
solve()




