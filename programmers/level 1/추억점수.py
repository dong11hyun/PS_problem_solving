def solution(name, yearning, photo):
    answer = []
    score_map = dict(zip(name,yearning))
    for p in photo :
        num = 0
        for person in p :
            num = num + score_map.get(person,0)
        answer.append(num)
    return answer