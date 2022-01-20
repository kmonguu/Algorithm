# 자연수 n이 매개변수로 주어지고, n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 반환

# 내가 푼 코드
# 자연수 n의 3진법 값을 answer에 담고, for문에서 3진법상에서 뒤집은 배열을 순회하며 10진법으로 계산한 값을 반환한다.

def solution(n):
    answer = ''
    
    while 0 < n:
        n, mod = divmod(n, 3)
        answer += str(mod)

    idx = 0
    result = 0
    for i in answer[::-1]:
        result += int(i) * 3 ** idx
        idx += 1
    return result




# 코드 수정 : n진수에서 10진수로 변환할 때, int(n진수, n)으로 한번에 10진수로 바꿀 수 있다.

def solution(n):
    answer = ''
    while 0 < n:
        n, mod = divmod(n, 3)
        answer += str(mod)
    
    return int(answer, 3)



# 다른 사람 코드

def convert(n, base):
    result = ""
    while n:
        result += str(n % base)
        n //= base
    
    return result

def solution(n):
    return int(convert(n, 3), 3)
