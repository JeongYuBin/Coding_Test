def solution(x):
    answer = True
    original = x
    thous, hund, ten, one = 0, 0, 0, 0
    if x==10000:
        return answer
    if x >= 1000:
        thous = x // 1000
        x %= 1000
    if x >= 100:
        hund = x // 100
        x %= 100
    if x >= 10:
        ten = x // 10
        x %= 10
    one = x
    
    val = thous + hund + ten + one
    
    if original % val == 0:
        answer = True
    else:
        answer = False
    return answer