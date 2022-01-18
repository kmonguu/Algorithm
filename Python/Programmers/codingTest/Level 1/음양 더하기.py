# 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개 변수로 주어질 때
# 실제 정수들의 합을 구하여 반환, True는 양수를 의미하며 False는 음수를 의미한다.

# 내가 푼 코드
# 두 배열의 각 요소를 x와 y로 zip 함수를 이용하여 묶어준다.
# if else 삼항 연산자를 이용하여 불리언 배열의 요소가 담긴 y가 False라면 x의 값을 -x로, True라면 x 그대로 새 배열 arr에 담고 그 합을 구한다.

def solution(absolutes, signs):
    arr = []
    for x, y in zip(absolutes, signs):
        arr.append(-x) if not y else arr.append(x)

    return sum(arr)
  
