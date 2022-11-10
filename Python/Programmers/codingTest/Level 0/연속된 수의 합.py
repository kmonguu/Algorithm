# 연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 두 정수 num과 total이 주어집니다. 
# 연속된 수 num개를 더한 값이 total이 될 때, 정수 배열을 오름차순으로 담아 반환

# 예제
# num | sum
# 3	  |  12	-> [3, 4, 5]
# 5   |  15	-> [1, 2, 3, 4, 5]
# 4   |  14	-> [2, 3, 4, 5]



# 내가 푼 코드

    answer = []
    middle = total//num


    if num % 2 == 0:
        answer.append(middle)
        answer.append(middle+1)

        for _ in range(num//2 -1):
            first, last = answer[0], answer[-1]
            answer.insert(0, first-1)
            answer.append(last+1)


    else:
        answer.append(middle)
        for _ in range(num//2):
            first, last = answer[0], answer[-1]
            answer.insert(0, first-1)
            answer.append(last+1)


    return answer
  
  
# 다른 사람 풀이
def solution(num, total):
    answer = []
    middle = total//num
    
    if num % 2 == 1:
        for i in range(middle-num//2, middle+num//2+1):
            answer.append(i)
            
    else:
        for i in range(middle-num//2+1, middle+num//2+1):
            answer.append(i)
            
    return answer
