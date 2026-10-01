def solution(new_id):
    answer = ''
    for i in new_id:
        # 1단계
        if i >= 'A' and i <='Z':
            val = ord(i) + 32
            answer += chr(val)
        else:
            answer += i
    # 2단계
    temp = ''
    for i in answer:
        if ('a'<= i <= 'z') or ('0' <= i <= '9') or i in ['-', '_', '.']:
            temp += i
    answer = temp
    # 3단계
    while ".." in answer:
        answer = answer.replace("..", ".")
    # 4단계
    # if answer -> answer가 빈 문자열인지 확인하기 
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if answer == '':
        answer += 'a'
    # 6단계 
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    while len(answer) < 3:
        temp = answer[-1]
        answer += temp
     
    return answer