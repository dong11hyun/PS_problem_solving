import sys
input = sys.stdin.readline

n, m = map(int, input().split())
id_to_name = {} # 숫자 -> 이름 
name_to_id = {} # 이름 -> 숫자 =검색 속도 O(1)
answer = []
        
for i in range(1, n + 1): 
    name = input().strip()
    id_to_name[i] = name  # 숫자 키 -> 이름 값
    name_to_id[name] = i  # 이름 키 -> 숫자 값
            
for _ in range(m):
    query = input().strip()
    answer.append(query)

for k in answer:    
    if k.isdigit():
        print(id_to_name[int(k)])
    else:
        print(name_to_id[k])
