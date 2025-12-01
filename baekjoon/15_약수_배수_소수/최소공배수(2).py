#silver 5

n,m = map(int,input().split())
def max_gongyak(n,m):
    while m > 0:
        n,m = m,n %m
    return n
def min_gongbae(n,m):
    return (n*m) // max_gongyak(n,m)
max_gongyak(n,m)
print(min_gongbae(n,m))
