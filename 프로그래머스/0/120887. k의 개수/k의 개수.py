def solution(i, j, k):
    answer = 0
    # i부터 j까지 k가 몇 번 등장하는지 
    for a in range(i, j+1):
        a = str(a)
        answer += a.count(str(k))
    return answer