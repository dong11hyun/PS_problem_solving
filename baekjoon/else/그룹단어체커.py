import sys
input = sys.stdin.readline
def is_group_word(word):
    for i in range(len(word) - 1):
        if word[i] != word[i+1]:
            if word[i] in word[i+1:]:
                return False
    return True

def solve():
    n = int(input())
    group_word_count = 0
    
    for _ in range(n):
        word = input().strip()
        if is_group_word(word):
            group_word_count += 1
            
    print(group_word_count)

solve()