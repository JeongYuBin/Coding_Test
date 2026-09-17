def solution(signals):
    answer = 0
    limit = 1 
    for i in range(len(signals)):
        G, Y, R = signals[i]
        val = G+Y+R
        limit *= val

    for t in range(1, limit+1):
        all_yellow = True
        # 모든 신호등 확인
        for sig in signals:
            G, Y, R = sig
            cycle = G+Y+R
            pos = (t-1)%cycle
            # 노란색
            if not (G <= pos < G+Y):
                all_yellow = False
                break
        if all_yellow:
            return t   
    return -1