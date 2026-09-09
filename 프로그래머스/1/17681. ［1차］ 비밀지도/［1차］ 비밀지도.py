def solution(n, arr1, arr2):
    answer = []
    arr1_map = []
    arr2_map = []
    # 지도 매핑하기 10진수를 2진수로 매핑하기 
    for i in arr1:
        dump = [0]*n
        check = -1
        while i != 0:
            val = i % 2
            dump[check] = val
            check -= 1
            i //= 2
        arr1_map.append(dump)
    for j in arr2:
        dump = [0]*n
        check = -1
        while j != 0:
            val = j % 2
            dump[check] = val
            check -= 1
            j //= 2
        arr2_map.append(dump)
        
    for i in range(len(arr1_map)):
        word = ''
        for j in range(len(arr1_map[0])):
            if arr1_map[i][j] == 1 or arr2_map[i][j] == 1:
                word += '#'
            else:
                word += " "
        answer.append(word)
    return answer