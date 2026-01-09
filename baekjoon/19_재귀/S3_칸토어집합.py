import sys

def cantor(n):
    if n == 0:
        return "-"
    
    # 전 단계의 칸토어 집합 구하기
    prev = cantor(n-1)
    
    # 공백의 길이는 3**(n-1)
    spaces = " " * (3 ** (n-1))
    
    # [전 단계] + [공백] + [전 단계]
    return prev + spaces + prev

def solve():
    # 입력이 끝날 때까지 계속 읽음 (EOF 처리)
    lines = sys.stdin.readlines()
    
    for line in lines:
        if not line:
            break
        n = int(line.strip())
        print(cantor(n))

if __name__ == "__main__":
    solve()
