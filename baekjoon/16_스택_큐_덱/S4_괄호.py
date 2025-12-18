def main():
    data = list(input().strip())
    check = []

    for i in data:
        if i == '(':
            check.append(i)
        elif i == ')':
            if check and check[-1] == '(':
                check.pop()
            else:
                check.append(i)
    if not check:  
        print("YES")
    else:
        print("NO")

n = int(input())
for i in range(n):
    main()


 
     