def is_star(i,j):
    while i > 0 and j > 0:
        if i % 3 == 1 and j % 3 == 1:
            return False
        i = i // 3
        j = j // 3
    return True

n = int(input())
for i in range(n):
    a = ""
    for j in range(n):
        if is_star(i,j):
            a += "*"
        else:
            a += " "
    print(a)