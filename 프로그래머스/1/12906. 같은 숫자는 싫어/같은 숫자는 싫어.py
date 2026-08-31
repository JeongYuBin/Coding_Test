def solution(arr):
    answer = []
    for i in range(len(arr)):
        check = arr[i]
        if i == 0:
            answer.append(arr[i])
        elif arr[i-1] == arr[i]:
            continue
        elif arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer