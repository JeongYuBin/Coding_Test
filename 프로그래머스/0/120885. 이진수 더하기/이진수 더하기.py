def solution(bin1, bin2):
    answer = 0
    result = ''
    for i in range(len(bin1)):
        if bin1[-(i+1)] =='1':
            answer += 2**i
    for i in range(len(bin2)):
        if bin2[-(i+1)] == '1':
            answer += 2**i  
    if answer == 0:
        return "0"
    while answer >0:  
        result = str(answer%2) + result  
        answer //= 2  
    
    return result