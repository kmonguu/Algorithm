# 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
# 수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 반환

# 예제
# quiz                                            result
# ["3 - 4 = -3", "5 + 6 = 11"]                  ["X", "O"]
# ["19 - 6 = 13", "5 - 15 = 63", "3 - 1 = 2"]   ["O", "X", "O"]

# 내가 푼 코드
# 사칙연산 식을 문자열로 받아서 실행하는 eval함수를 사용하여 배열에 저장된 수식이 맞는지 판별함

def solution(quiz):
    answer = []
    for i in quiz:
        calc = i.split('=')
        answer.append('O' if eval(calc[0]) == eval(calc[1]) else 'X')
    return answer
