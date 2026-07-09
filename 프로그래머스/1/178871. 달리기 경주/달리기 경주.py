def solution(players, callings):
    
    rank = {}
    for i in range(len(players)):
        rank[players[i]] = i
        
    for call in callings:
        idx = rank[call]
        front = players[idx-1] # 앞 선수
        players[idx-1], players[idx] = players[idx], players[idx-1]
        
        rank[call] -= 1
        rank[front] += 1
    
    return players

