def solution(wallpaper):
    a, b, c, d = -1, len(wallpaper[0]), -1, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if a == -1:
                    a = i
                if i >= c:
                    c = i+1
                if j <= b:
                    b = j
                if j >= d:
                    d = j+1
    return [a,b,c,d]