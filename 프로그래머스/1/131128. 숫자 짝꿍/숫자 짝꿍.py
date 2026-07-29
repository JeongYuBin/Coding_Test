# X값들을 담을 배열
# Y값들을 담을 배열
# X랑 Y랑 하나씩 비교해서 같은 것을 담는 배열 -> 같은것이 생기면 배열에서 지우기 .remove()하면 맨 앞에 있는 것부터 삭제 
# 같은 것은 배열에 넣은 뒤, 해당 갓들에 대해서 sort 진행하기 꺼내서 하나씩 더하기
# # -> 시간 초과 발생

# def solution(X, Y):
#     x_arr = []
#     y_arr = []
#     same_arr = []
#     answer = ''
    
#     # X추출
#     for i in range(len(X)):
#         x_arr.append(X[i])
#     # Y추출
#     for j in range(len(Y)):
#         y_arr.append(Y[j])
#     # 같은 것 찾기
#     # [:] -> 복사본 만들기(remove를 해도 영향이 가지 않음)
#     for a in x_arr[:]:
#         for b in y_arr[:]:
#             if a==b:
#                 same_arr.append(int(a))
#                 x_arr.remove(a)
#                 y_arr.remove(b)
#                 break
#     same_arr.sort(reverse=True)
    
#     if not same_arr:
#         return "-1"
    
#     if same_arr[0] == 0:
#         return "0"
    
#     for k in range(len(same_arr)):  
#         answer+=str(same_arr[k])
    
#     return answer


# 2.
def solution(X, Y):
    answer = ''

    # 9부터 0까지 내림차순으로 각 숫자 개수 구하기
    for number in range(9, -1, -1):
        number_str = str(number)

        # 공통된 숫자의 개수(가장 작은 숫자로 정하기)
        common_count = min(
            X.count(number_str),
            Y.count(number_str)
        )

        answer += number_str * common_count

    if answer == '':
        return '-1'

    if answer[0] == '0':
        return '0'

    return answer

