# 큰 수의 법칙 
# 주어진 수들을 m번 더해서 가장 큰수를 만든다. 특정 인덱스 번호가 k번 초과해서 더하는거 불가능
# n = 배열의 크기 / m = 숫자가 더해지는 횟수 / k = 특정 인덱스 번호 더해지는 횟수.
n, m, k = map(int, input().split())    # 5 8 3
data = list(map(int, input().split())) # 2 4 5 4 6
data.sort()                            # 2 4 4 5 6
first =  data[n-1]                     # 6
second = data[n-2]                     # 5
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second
    m -= 1

print(result)

## 수학적인 계산 이용

count = int(m/(k+1)) * k
count += m % (k+1)
result = 0
result += (count) * first #가장 큰 수 더하기
result += (m-count) * second #두번째로 큰수 더하기



