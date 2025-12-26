from collections import deque
n, k = map(int, input().split())
queue = deque()
answer = []
for i in range(1,n+1):
    queue.append(i)
while len(queue):
    for j in range(k):
        if j < k-1:
            queue.append(queue.popleft())
        else :
            answer.append(queue.popleft())
        

print(f"<{', '.join(map(str, answer))}>")

