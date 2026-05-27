def solution(my_string):
    answer = 0
    buffer = ''

    for i in my_string:
        if '0' <= i <= '9':
            buffer += i
        else:
            if buffer != '':
                answer += int(buffer)
                buffer = ''

    if buffer != '':
        answer += int(buffer)

    return answer



# def solution(my_string):
#     answer = 0
#     buffer = ''
#     my_string = list(my_string)
#     for i in my_string:
#         if 'A' <= i <='z':
#             answer = answer + int(buffer)
#             buffer = 0
#             continue
#         else:
#             buffer.append(i)
    
#     return answer + int(buffer)