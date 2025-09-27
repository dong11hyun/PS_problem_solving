n, k = map(int, input().split())
count = 0

while n != 1:
    if n % k == 0:
        n //= k  # 정수 나눗셈(//)을 사용하는 것이 더 안전
        count += 1
    else:
        n -= 1
        count += 1
print(count)

        
    

