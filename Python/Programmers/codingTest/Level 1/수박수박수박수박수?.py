# 길이가 n이고 '수박수박수박수..'와 같은 패턴을 유지하는 문자열을 반환

# 내가 푼 코드
# '수'와 '박'을 배열 안에 넣고, 0부터 매개변수로 주어지는 정수 n까지 순회하며,
# 짝수라면 '수'를 answer에 저장, 홀수라면 '박'을 answer에 저장한다.

def solution(n):
    answer = ''
    
    arr = ['수', '박']
    for i in range(n):
        if i % 2 == 0:
            answer += arr[0]
        else:
            answer += arr[1]
    return answer
        

    
# 다른 사람 풀이
# 문자열 곱하기를 활용한 방법
# n이 홀수인 경우를 (n+1)//2로 처리

def solution(n):
    return ("수박" * ((n + 1) // 2))[:n]
