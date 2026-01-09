import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)      # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)        # 병합

def merge(A, p, q, r):
    global count, result
    i = p
    j = q + 1
    tmp = []
    
    # 1. 두 그룹을 비교하여 작은 순서대로 임시 리스트에 저장
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    
    # 2. 남은 원소들 처리
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    
    # 3. 원본 배열 A에 정렬된 내용 덮어쓰기 (문제의 핵심 포인트)
    i = p
    t = 0
    while i <= r:
        A[i] = tmp[t]
        count += 1
        if count == K:  # K번째 저장되는 순간을 포착
            result = A[i]
        i += 1
        t += 1

# 입력 처리
N, K = map(int, input().split())
A = list(map(int, input().split()))

count = 0 
result = -1

merge_sort(A, 0, N - 1)

print(result)


