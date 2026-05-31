def solution(polynomial):
    answer = ''
    x_count = 0
    num = 0
    polynomial = polynomial.split(' ')
    for i in polynomial:
        if i == '+':
            continue
        if 'x' in i:
            if i == 'x':
                x_count += 1
            else :
                x_count += int(i[:-1])  # 마지막 글자를 빼고 가져오기 
        else: 
            num += int(i)
    
    if x_count > 0:
        if x_count ==1 :
            answer += 'x'
        else:
            answer += str(x_count)+'x'
    if num > 0:
        if answer != '':  # answer 가 비어있지 않으면 
            answer += ' + '
        answer += str(num)
        
    return answer