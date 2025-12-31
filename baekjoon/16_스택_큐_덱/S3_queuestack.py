import sys
from collections import deque

# 1. 빠른 입력 설정
input = sys.stdin.readline

# 2. 입력 데이터 받기
N = int(input())                            # 자료구조 개수
A = list(map(int, input().split()))         # 자료구조 형태 (0:큐, 1:스택)
B = list(map(int, input().split()))         # 초기값
M = int(input())                            # 삽입할 수열 길이
C = list(map(int, input().split()))         # 삽입할 값들

# 3. 핵심 로직: 큐(0)인 것만 골라서 Deque에 넣기
queue_store = deque()

for i in range(N):
    if A[i] == 0:
        # 큐에 있는 값은 나중에 들어온 놈(인덱스 큰 놈)이 먼저 나가므로
        # 왼쪽에 붙여줍니다. (출구 방향)
        queue_store.appendleft(B[i])


for val in C:
    queue_store.append(val)

# 5. 앞에서부터 M개만큼만 꺼내서 출력하면 끝입니다.
# popleft()를 쓰면 앞에서부터 하나씩 나옵니다.
for i in range(M):
    print(queue_store.popleft(), end=' ')