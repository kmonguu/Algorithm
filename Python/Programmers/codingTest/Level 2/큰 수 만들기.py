# 문자열 형식으로 숫자 number와 제거할 수의 개수 k가 주어질 때,
# number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 반환

# 예제
# 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있다.
# 이 중 가장 큰 수 '94'가 반환

# 내가 푼 코드 (인터넷 참고)

def solution(number, k):
    answer = [] 
    
    for num in number:
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
        
    return ''.join(answer[:len(answer) - k])
