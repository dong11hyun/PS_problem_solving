import sys
input = sys.stdin.readline
n= int(input())
loc = []
gcd = []
def gcd_max(a,b):
    while b>0:
        a,b=b,a%b
    return a

for i in range(n):
    loc.append(int(input()))
for j in range(len(loc)-1):
    gcd.append(loc[j+1]-loc[j])

g = gcd[0]
for k in range(1,len(gcd)):
    g = gcd_max(g,gcd[k])
ans = 0
for gcdd in gcd:
    ans += gcdd//g -1
print(ans)


