n,m = map(int, input().split())
result = []

def back(k):
    if k == m:
        print(*result)
        return

    for i in range(1,n+1): 
        if True:
            result.append(i)
            back(k+1)
            result.pop()

back(0)