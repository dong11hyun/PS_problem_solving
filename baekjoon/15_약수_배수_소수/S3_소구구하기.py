n,m = map(int, input().split())

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return x

for i in range(n,m+1):
    if is_prime(i): # i가 소수(True)라면
        print(i)
        

