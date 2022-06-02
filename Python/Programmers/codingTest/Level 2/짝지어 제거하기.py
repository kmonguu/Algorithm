# 짝지어 제거하기는, 알파벳 소문자로 이루어진 문자열을 가지고 시작        -> [baabaa]
# 먼저 문자열에서 같은 알파벳이 2개 붙어 있는 짝을 찾습니다.            -> b aa baa
# 그다음, 그 둘을 제거한 뒤, 앞뒤로 문자열을 이어 붙입니다.            -> bb aa
# 이 과정을 반복해서 문자열을 모두 제거한다면 짝지어 제거하기가 종료됩니다. -> aa


# 내가 푼 코드
# 스택을 이용하여 check라는 빈 배열을 두고, s 배열에 저장된 문자를 하나씩 check로 옮기며 비교하여 삭제하는 식으로 품
# check       s
# []          [baabaa]    -> check가 빈배열이므로 s를 pop하여 check에 담음
# [a]         [baaba]     -> check[-1]과 s[-1]을 비교하여 같다면 삭제
# []          [baab]      -> check가 빈배열이므로 s를 pop하여 check에 담음
# [b]         [baa]       -> check[-1]과 s[-1]을 비교하여 같지 않다면 s를 pop하여 check에 담아줌
# [ba]        [ba]        -> check[-1]과 s[-1]을 비교하여 같다면 삭제하는 것을 반복하면 짝지어 제거하기가 성공적으로 끝남, 1을 반환한다.


def solution(s):
    answer = 0
    s = list(s)
    check = []
    while s:
        if len(check) == 0:
            check.append(s.pop())
        else:
            if check[-1] == s[-1]:
                check.pop()
                s.pop()
            else:
                check.append(s.pop())

    return 0 if check else 1
