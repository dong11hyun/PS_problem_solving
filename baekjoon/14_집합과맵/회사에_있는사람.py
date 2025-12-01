import sys
input = sys.stdin.readline

n = int(input())
original = set()

for _ in range(n):
    string = input().strip()
    if string.endswith('leave'):
        prefix = string.replace(" leave", "")
        original.discard(prefix + " enter")
    else :     
        original.add(string)

my_list = sorted(original, reverse = True)

for word in my_list:
    print(word[:-5])
