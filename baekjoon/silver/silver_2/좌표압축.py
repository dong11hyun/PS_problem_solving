import sys
input = sys.stdin.readline  

n = int(input())
original = list(map(int, input().split()))

original_set = set(original)
before_sort_list = list(original_set)
sort_list = sorted(before_sort_list)

compress = {}
for idx,value in enumerate(sort_list):
    compress[value] = idx

result = []
for i in original:
    result.append(compress[i])

print(result)
    
