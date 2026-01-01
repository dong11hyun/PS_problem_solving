n = int(input())
data = list(map(int, input().split())) #data 저장

data_set = set(data)

if n == 1 :
    (value,) = data_set
    print(value * value)
else :
    print(min(data_set) * max(data_set))