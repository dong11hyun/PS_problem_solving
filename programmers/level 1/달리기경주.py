## 달리기경주.. 시간초과떳음 -> 
players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
for call in callings:
    location = players.index(call)  #이부분에서 시간초과 M * N
    if location == 0:
        pass
    else:
        A = players[(location-1)]
        players[(location-1)] = players[location]
        players[location] = A
print(players)

def solution(players, callings):
    #딕셔너리 컴프리헨션- enumerate(players) == (0,mumu),(1,soe)...
    player_map = {player : i for i, player in enumerate(players)}
    

    for called_player in callings:
        # 3. 호명된 선수의 현재 등수를 O(1)만에 조회
        current_idx = player_map[called_player]
        # 4. 바로 앞 선수 정보 조회
        front_player = players[current_idx - 1]
        # 5. players 리스트에서 두 선수의 위치 변경 (swap)
        players[current_idx - 1], players[current_idx] = players[current_idx], players[current_idx - 1]
        # 6. (핵심) 딕셔너리의 등수 정보 업데이트
        player_map[called_player] -= 1
        player_map[front_player] += 1
    return players