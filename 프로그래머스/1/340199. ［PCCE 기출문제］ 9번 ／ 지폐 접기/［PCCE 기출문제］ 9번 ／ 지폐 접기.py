def solution(wallet, bill):
    answer = 0
    trigger = True
    while trigger:
        if bill[0] >= bill[1]:
            if bill[0] > max(wallet):
                bill[0] //= 2
                answer += 1
            elif bill[1] > min(wallet):
                bill[0] //= 2
                answer += 1
            else:
                trigger = False
        elif bill[0] < bill[1]:
            if bill[1] > max(wallet):
                bill[1] //= 2
                answer += 1
            elif bill[0] > min(wallet):
                bill[1] //= 2
                answer +=1
            else:
                trigger = False
    return answer