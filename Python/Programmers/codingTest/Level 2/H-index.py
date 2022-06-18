# 어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index이다.
# 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 반환

# 내가 푼 코드
# 1부터 citations배열의 길이만큼 for문으로 반복하여 내림차순으로 정렬된 citations 배열과 비교했을 때,
# for문으로 반복되고 있는 논문의 번호보다 참조된 횟수가 더 작다면 
# 참조된 횟수가 더 큰 값 중의 최댓값을 반환한다.
# 만약, 모든 참조가 논문의 번호보다 크다면 마지막 논문의 번호를 반환한다.

def solution(citations):
    citations.sort(reverse = True)
    
    for num in range(1, len(citations)+1):
        if num > citations[num-1]:
            return num-1
    return len(citations)
