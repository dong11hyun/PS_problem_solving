#백준 14888번
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
yeon = list(map(int, input().split()))
maximum = 0
minimum = 0
def back(k, current_val):
    global maximum, minimum, yeon
    if k == n:
        maximum = max(maximum, current_val)
        minimum = min(minimum, current_val)
        return
    for i in range(4):
        if yeon[i] > 0:
            yeon[i] -= 1
            if i == 0:
                back(k + 1, current_val + data[k])
            if i == 1:
                back(k + 1, current_val - data[k])
            if i == 2:
                back(k + 1, current_val * data[k])
            if i == 3:
                back(k + 1, current_val / data[k])

back(0,0)
print(maximum)
print(minimum)