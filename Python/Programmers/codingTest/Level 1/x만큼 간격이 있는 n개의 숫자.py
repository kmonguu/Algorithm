# 정수 x와 자연수 n을 입력 받아, x부터 시작하여 x씩 증가하는 숫자를 n개 지니는 리스트를 반환

# 나의 코드
# plus라는 변수에 x값을 넣고 answer의 길이가 n이 될 때까지 x에 plus 누적합을 구하여 담는다.
def solution(x, n):
    answer = []
    plus = x
    while len(answer) < n:
        answer.append(x)
        x += plus
    return answer
  
  
# 다른 사람 코드
# 등차수열의 공식을 적용

def solution(x, n):
    return [x * i for i in range(1, n+1)]




# range 함수를 이용한 방법
# 범위의 마지막 값을 x * (n+1)로 하여 양수와 음수일 때 처리되도록 하고, x가 0인 경우 [0] * n 을 반환

def solution(x, n):
    return list(range(x, x * (n + 1), x)) if x else [0] * n
