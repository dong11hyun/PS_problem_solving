
n,m = map(int, input().split())
result = []
def back(k,s):
    if k == m:
        print(*result)
        return

    for i in range(s,n+1): 
        if i not in result:
            result.append(i)
            back(k+1,i+1)
            result.pop()

back(0,1)
