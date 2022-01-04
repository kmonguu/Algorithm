# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수를 반환하는 문제


# 풀이
# 처음엔 set으로 접근했지만 동명이인을 처리하지 못함
# 다른 사람의 풀이를 참고하여 collections 모듈을 사용한 방법과 for문을 통해 두 인덱스를 비교하는 방법으로 풀 수 있었다.


# 방법 1
# value와 key값이 수를 세어 참여자에서 완주자 배열을 빼고 남은 값은 완주하지 못한 사람이 된다.
# 연산 과정에서 key 값이 0이면 사라지므로 값이 남은 요소는 0 번째자리로 오게 된다.
import collections

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer)[0]

  
# 방법 2
# completion 배열의 길이만큼 participant에서 없는 사람을 찾는 방법

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
