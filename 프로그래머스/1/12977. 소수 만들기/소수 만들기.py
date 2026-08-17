def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                val = nums[i]+nums[j]+nums[k]
                check = 0
                for t in range(2, val):
                    if val % t == 0:
                        check = 1
                        break
                if check == 0:
                    answer +=1
                        
    return answer