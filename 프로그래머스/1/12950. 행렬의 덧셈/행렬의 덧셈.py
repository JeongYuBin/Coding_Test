def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        row = []  # 행
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        answer.append(row)
            
            
    return answer