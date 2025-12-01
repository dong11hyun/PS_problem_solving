import sys
input = sys.stdin.readline

n = int(input())
user_card = list(map(int, input().split()))
m = int(input())
check_card = list(map(int, input().split()))

user_card_set = set(user_card)
answer = []

for i in check_card:
    if i in user_card_set:
        answer.append(1)
    else :
        answer.append(0)
        
print(*answer)