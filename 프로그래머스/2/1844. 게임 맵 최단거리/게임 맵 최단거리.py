def solution(maps):
    answer = 0
    # S, W, E, N
    loc =  [[1, 0], [0, -1], [0, 1], [-1, 0]]
    queue = [[0, 0]]
    while queue:
        x, y = queue.pop(0)
        for dx, dy in loc:
            nx = x + dx
            ny = y + dy
            # 맵 안에 있는지 확인
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append([nx, ny])
    if maps[-1][-1] == 1:
        return -1
        
    return maps[-1][-1]