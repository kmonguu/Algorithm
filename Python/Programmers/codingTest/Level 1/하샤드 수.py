# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 한다.
# 예를 들어, 18의 자릿수 합은 1 + 8 = 9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수이다.

# 내가 푼 코드
# 매개변수로 들어오는 양의 정수 x를 문자열로 바꾸고 한 자리씩 int로 리스트에 저장하여 합을 구한다.
# if else 삼항연산자를 이용하여 양의 정수 x와 자릿수의 합 a가 나누어떨어지면 True를 반환, 아니면 False를 반환하도록 한다.

def solution(x):
    a = sum([int(i) for i in str(x)])
    return True if x % a == 0 else False



# 다른 사람 코드

def solution(x):
    return x % sum([int(i) for i in str(x)]) == 0



# map, sum 함수를 이용해서 각 자리수의 합 구하는 방법, bool 함수를 이용해서 해당 값을 True, False로 변환

def solution(x):
    return bool(not x % sum(map(int, str(x))))
