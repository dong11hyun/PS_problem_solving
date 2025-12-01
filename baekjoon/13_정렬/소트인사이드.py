#1427번
n = (input())
array = []
for i in n:
    array.append(int(i))
array.sort(reverse=True)
answer = ''
for j in array:
    answer+=str(j)
print(answer)


n=int(input())
n=sorted(str(n),reverse=True)

for i in n:
    print(int(i),end='')