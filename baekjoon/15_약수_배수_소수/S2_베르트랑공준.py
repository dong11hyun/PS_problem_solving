import sys
input = sys.stdin.readline
LIMIT = 123456 * 2
is_prime_list = [True] * (LIMIT + 1) #전부다 소수라고 리스트 먼저 선언 및 가정
is_prime_list[0] = False 
is_prime_list[1] = False 


for i in range(2, int(LIMIT**0.5) + 1):
    if is_prime_list[i]: 
        for j in range(i * i, LIMIT + 1, i):
            is_prime_list[j] = False

print(is_prime_list)

while True:
    n = int(input())
    if n == 0:
        break
    count = sum(is_prime_list[n+1 : 2*n + 1])
    print(count)