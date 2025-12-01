
def max_gongyak (a,b):
    while b > 0:
        a,b = b,a % b
    return a

def min_gongbae(a,b):
    return (a*b) // max_gongyak(a,b)

n = int(input())
answer = []
for i in range(n):
    A,B = map(int, input().split())
    max_gongyak(A,B)
    answer.append(min_gongbae(A,B))
for i in answer:
    print(i)