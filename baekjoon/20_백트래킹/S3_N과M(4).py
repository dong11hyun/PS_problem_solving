
n,m = map(int, input().split())
result = []
def back(k,s):
    if k == m:
        print(*result)
        return

    for i in range(s,n+1): 
        if True:
            result.append(i)
            back(k+1,i)
            result.pop()

back(0,1)
