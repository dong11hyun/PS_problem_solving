#특이한 정렬
# 1. sorted() 함수를 사용하여 numlist를 정렬합니다.
    # 2. key 인자에 lambda 함수를 전달하여 커스텀 정렬 기준을 정의합니다.
    #    - lambda x: 각 원소 x에 대해 적용할 함수
    #    - (abs(x - n), -x): 정렬 기준이 되는 튜플
    #      - 첫 번째 기준: n과의 거리(abs(x - n)). 이 값을 기준으로 오름차순 정렬.
    #      - 두 번째 기준: 원소의 음수값(-x). 거리가 같을 경우 이 값을 기준으로 오름차순 정렬
    #        (결과적으로 원래 값 x는 내림차순 정렬됨).
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x-n), -x))
