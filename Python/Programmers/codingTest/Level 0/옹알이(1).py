# 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못한다.
# 문자열 배열 babbling이 매개변수로 주어질 때, 조카가 발음할 수 있는 단어의 수를 출력

# 예제
# ["aya", "yee", "u", "maa", "wyeoo"]-> 	1
# ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"] -> 	3

# 나의 풀이
# 각 단어를 돌면서 babbling에 포함된 단어는 공백처리 해주어 갯수를 구함

def solution(babbling):
    count = 9
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            count += 1
    return count
  
  
# 두번째 풀이
# 조합을 사용하여 만들 수 있는 단어를 조합하고 그 중 babbling이 있는지 찾는 방법

from itertools import permutations
def solution(babbling):
    answer = 0
    speek = ["aya","ye","woo","ma"]
    word = []
    for i in range(1, len(speek)+1):
        for j in permutations(speek, i):
            word.append(''.join(j))

    for i in babbling:
        if i in word:
            answer += 1

    return answer
