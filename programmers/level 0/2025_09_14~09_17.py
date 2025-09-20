#특이한 정렬
# 1. sorted() 함수를 사용하여 numlist를 정렬
    # 2. key 인자에 lambda 함수를 전달하여 커스텀 정렬 기준을 정의합니다.
    #    - lambda x: 각 원소 x에 대해 적용할 함수
    #    - (abs(x - n), -x): 정렬 기준이 되는 튜플
    #      - 첫 번째 기준: n과의 거리(abs(x - n)). 
    #      - 두 번째 기준: 원소의 음수값(-x).
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x-n), -x))

#다항식 더하기
def solution(polynomial):
    x_con = 0
    con = 0
    terms = polynomial.split(" + ")  #항들을 분리
    for term in terms:               #각 항 for문 돌면서 확인
        if 'x' in term:             #x항 인지 확인
            if term == 'x':
                x_con += 1
            else:
                x_con += int(term[:-1])
        else:                     #상수항   
            con += int(term)
    parts = []                  #결과 문자열 만들기
    if x_con > 0:
        if x_con == 1:
            parts.append("x")
        else:
            parts.append(f"{x_con}x") #f-string 
    if con > 0:
        parts.append(str(con))
        
    return ' + '.join(parts)   

#최빈값 구하기
from collections import Counter
def solution(array):
    counts = Counter(array) #배열 안 요소들 개수
    most_common_items = counts.most_common(2)#[(최빈값, 빈도수), (차빈값, 빈도수)]
    # Case 1: 배열에 숫자가 하나뿐이거나, 모든 숫자가 동일한 경우
    if len(most_common_items) == 1:
        return most_common_items[0][0]
    # Case 2: 최빈값의 빈도수와 두 번째로 흔한 값의 빈도수가 같은 경우
    # 즉, 최빈값이 여러 개인 경우
    if most_common_items[0][1] == most_common_items[1][1]:
        return -1
    # Case 3: 최빈값이 유일한 경우
    else:
        return most_common_items[0][0] 
    
    #OX퀴즈
    def solution(quiz):
        answer = []
        for i in quiz:
            k = i.split(" ")
            if k[1] == '+':
                if int(k[0]) + int(k[2]) == int(k[4]):
                    answer.append("O")
                else:
                    answer.append("X")
            if k[1] == '-':
                if int(k[0]) - int(k[2]) == int(k[4]):
                    answer.append("O") 
                else:
                    answer.append("X")
        
        return answer


