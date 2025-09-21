# 거스름돈 문제
n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n // coin # 해당화폐로 거슬러 줄수 있는 동전의 개수 세기
    n %= coin

print(count)

# 시간복잡도 O(k) k는 화폐종류