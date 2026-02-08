ans = [0] * (101)
ans[1] = 1
ans[2] = 1
ans[3] = 1
ans[4] = 2
ans[5] = 2
ans[6] = 3
ans[7] = 4
ans[8] = 5

for i in range(9,101):
    ans[i] = ans[i-1]+ans[i-5]

n = int(input())
for i in range(n):
    p = int(input())
    print(ans[p])

