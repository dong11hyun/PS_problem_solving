def solution(keymap, targets):
    min_cost_map = {}
    for key_string in keymap:
        for i, char in enumerate(key_string):
            cost = i + 1
            if char not in min_cost_map or cost < min_cost_map[char]:
                min_cost_map[char] = cost
    result=[]
    for target in targets:
        sum = 0
        for char in target:
            if char not in min_cost_map:
                sum = -1
                break
            sum += min_cost_map[char]
        result.append(sum)
    return result

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
print(f"결과: {solution(keymap, targets)}") # 예상 결과: [9, 4]

keymap2 = ["AGZ", "BSSS"]
targets2 = ["ASA","BGZ"]
print(f"결과: {solution(keymap2, targets2)}") # 예상 결과: [4, 6]