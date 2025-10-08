#9506번

n = int(input())
result = []
for i in range(1,n):
    if n % i == 0:
        result.append(i)

result_map = ' + '.join(map(str, result))

if sum(result) == n:
    print(f"{n} = {result_map}")
else : 
    print(f"{n} is NOT perfect.")