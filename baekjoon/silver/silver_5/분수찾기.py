# 1193 번
x = int(input())
line = 1
while x > line:
    x -= line
    line += 1

if line % 2 == 0:  # 짝수 라인
    top = x
    bottom = line - x + 1
else:  # 홀수 라인
    top = line - x + 1
    bottom = x

print(f"{top}/{bottom}")
