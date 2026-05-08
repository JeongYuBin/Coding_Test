def solution(balls, share): # ballsCshare
    bunja = 1
    bunmo = 1
    bunmo_2 = 1
    t = balls - share
    for i in range(1, balls+1):
        bunja *= i
        if i <= share:
            bunmo *= i
        if i <= t:
            bunmo_2 *= i
    answer = bunja // (bunmo * bunmo_2)
    
    return answer