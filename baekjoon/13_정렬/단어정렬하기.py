import sys
input = sys.stdin.readline

n = int(input())
words_set = set()

for _ in range(n):
    word = input().rstrip() 
    words_set.add(word)

words = list(words_set)

words.sort(key = lambda x : (len(x),x))
for word in words:  
    print(word)

#or sort의 안정정렬..
#word.sort()
#word.sort(key = len)