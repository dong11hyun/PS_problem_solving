# 1부터 3까지 자연수 중에서 중복없이 m개를 고른 수열
# 3 1  1부터 3까지 자연수 중에서 중복없이 1개를 고른 1,2,3
# 4 2   1부터 4까지  중복없이 2개를 고른 수열..
# 1 2 / 1 3 / 1 /4

n,m = map(int, input().split())
result = []
def back(k):
    if k == m:
        print(*result)
        return

    for i in range(1,n+1): 
        if i not in result:
            result.append(i)
            back(k+1)
            result.pop()

back(0)
