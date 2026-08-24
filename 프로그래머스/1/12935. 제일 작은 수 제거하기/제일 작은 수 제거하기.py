def solution(arr):
    check = arr[0]
    for i in range(len(arr)):
        if arr[i] <= check:
            check = arr[i]
    arr.remove(check)
    if len(arr) == 0:
        return [-1]
    return arr