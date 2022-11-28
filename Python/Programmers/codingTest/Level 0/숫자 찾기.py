# 정수 num과 k가 매개변수로 주어질 때, num을 이루는 숫자 중에 k가 있으면 num의 그 숫자가 있는 자리 수를 return하고 없으면 -1을 반환

# 내가 푼 코드
# 매개변수로 주어지는 num과 k는 숫자이므로 각각 문자열로 변환 후, find()함수로 num안에 k가 있는지 확인 후 반환

def solution(num, k):
    return int(str(num).find(str(k)))+1 if str(k) in str(num) else -1
      

