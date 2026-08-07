# 3진법 : n을 3으로 나눈 나머지 -> ex) n : 45 => 0021
# 0021을 10진수 -> 3^0*1 + 3^1 + 2 + .. 

def solution(n):
    answer = 0
    remain =''
    # 몫이 0이 되면 종료
    while n > 0:
        value = n%3
        remain += str(value)
        n //= 3
    for i in range(len(remain)):
        answer += 3**i*(int(remain[-1-i]))
        
    
    return answer