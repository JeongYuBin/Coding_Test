def solution(arr):
    answer = 0
    val = 0
    for i in range(len(arr)):
        val += arr[i]
    answer = val / len(arr)
    return answer