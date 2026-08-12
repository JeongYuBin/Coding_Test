# 중요! 여벌을 챙겨온 학생도 도난 당할 수 있다

def solution(n, lost, reserve):
    answer = 0
    used = []
    # 여벌 챙겨왔는데 도난 당한 사람
    for lo in lost[:]:
        if lo in reserve:
            lost.remove(lo)
            reserve.remove(lo)
    lost.sort()
    for lo in lost:
        if lo-1 in reserve and lo-1 not in used:
            used.append(lo-1)
        elif lo+1 in reserve and lo+1 not in used:
            used.append(lo+1)
    answer = n - len(lost) + len(used)
    
    return answer