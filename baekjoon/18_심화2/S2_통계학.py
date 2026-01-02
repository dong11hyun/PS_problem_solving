import sys
from collections import Counter

def solve():
    input = sys.stdin.readline
    n = int(input())
    nums = []
    total_sum = 0
    for _ in range(n):
        k = int(input())
        nums.append(k)
        total_sum += k

    print(round(total_sum / n))

    nums.sort()
    print(nums[n // 2])

    counter = Counter(nums)
    modes = counter.most_common()
    max_freq = modes[0][1]
    
    # 최빈값이 동일한 값들을 추출
    candidates = [val for val, freq in modes if freq == max_freq]
    
    # 최빈값 후보가 여러 개라면 두 번째로 작은 값(Index 1) 출력
    # (이미 nums가 정렬되어 있었으므로 candidates도 정렬된 상태나 다름없음)
    if len(candidates) > 1:
        candidates.sort() # 확실한 처리를 위해 정렬
        print(candidates[1])
    else:
        print(candidates[0])

    print(nums[-1] - nums[0])

solve()