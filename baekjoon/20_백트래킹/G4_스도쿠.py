#백준 2580번
import sys
input = sys.stdin.readline

def check(list):
    if sum(list) == 45:
        return
    list[list.index(0)] = 45 - sum(list)

data1 = list(map(int, input().split()))
check(data1)
data2 = list(map(int, input().split()))
check(data2)
data3 = list(map(int, input().split()))
check(data3)
data4 = list(map(int, input().split()))
check(data4)
data5 = list(map(int, input().split()))
check(data5)
data6 = list(map(int, input().split()))
check(data6)
data7 = list(map(int, input().split()))
check(data7)
data8 = list(map(int, input().split()))
check(data8)
data9 = list(map(int, input().split()))
check(data9)


