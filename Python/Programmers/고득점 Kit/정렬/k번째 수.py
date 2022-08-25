# 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 할 때, 
# 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때, commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 반환

# 예시
# array가 [1, 5, 2, 6, 3, 7, 4], command가 i = 2, j = 5, k = 3이라면

# array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]가 되고,
# [5, 2, 6, 3]에서 나온 배열을 정렬하면 [2, 3, 5, 6]이 된다.
# [2, 3 , 5, 6]에서 나온 배열의 3번째 숫자는 5가 되어 반환된다.
 
  
# 내가 푼 코드
#
def solution(array, commands):
    answer = []
    for i in commands:
        answer.append(sorted(array[i[0]-1: i[1]])[i[-1]-1])
    return answer
  
  
# 내가 이전에 푼 코드
# 이전에 비해 인덱스 슬라이싱에 대해 완전히 이해된 느낌이 들었음

def solution(array, commands):
    answer = []
    for idx in commands:
        arr = array[idx[0]-1 : idx[1]]
        arr.sort()
        answer.append(arr[idx[2]-1])
    return answer
