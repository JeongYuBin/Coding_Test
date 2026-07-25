# 1231 해당 숫자가 연속이어야함 -> 연속 일 경우 drop 하고 answer +=1 

def solution(ingredient):
    answer = 0
    stack = []
    for ingre in ingredient:
        stack.append(ingre)
        if len(stack) >= 4:
            if stack[-4:] == [1,2,3,1]:
                answer += 1
                for _ in range(4):
                    stack.pop(-1)     
                
    return answer