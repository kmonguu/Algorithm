# 정수 배열 array가 매개변수로 주어질 때, 7이 총 몇 개 있는지 반환

# 예제
[7, 77, 17]  4
[10, 29]     0

# 내가 푼 코드
# 배열에 저장된 숫자를 문자로 바꾸어 7이 포함된 개수를 count함

def solution(array):
    answer = 0
    for i in array:
        answer += str(i).count('7')
    return answer
