#특이한 정렬
def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x-n), -x))
