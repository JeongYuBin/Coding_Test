def solution(numbers):
    eng = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):  # 0~9 변경
        numbers = numbers.replace(eng[i], str(i))  # replace는 문자열 -> 문자열만 가능
        
    return int(numbers)

# python replace 함수
# replace(old, new)