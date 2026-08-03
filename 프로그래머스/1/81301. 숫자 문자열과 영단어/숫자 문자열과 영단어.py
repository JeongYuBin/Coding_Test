# def solution(s):
#     answer = ''
#     check = 0
#     while check < len(s):
#         if s[check] >= '0' and s[check] <= '9':
#             answer += s[check]
#             check += 1
#         elif s[check] == 'z':
#             answer += '0'
#             check += 4
#         elif s[check] == 'o':
#             answer += '1'
#             check += 3
#         elif s[check] == 'e':
#             answer +='8'
#             check += 5
#         elif s[check] =='n':
#             answer += '9'
#             check += 4
#         elif s[check] == 't':
#             if s[check+1] == 'w':
#                 answer += '2'
#                 check += 3
#             else:
#                 answer += '3'
#                 check += 5
#         elif s[check] == 'f':
#             if s[check+1] == 'o':
#                 answer += '4'
#                 check += 4
#             else:
#                 answer += '5'
#                 check += 4
#         elif s[check] == 's':
#             if s[check+1] == 'i':
#                 answer += '6'
#                 check += 3
#             else:
#                 answer += '7'
#                 check += 5
        
#     return int(answer)

def solution(s):
    
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    for key, value in num_dic.items():
        s = s.replace(key, value)

    return int(s)