# 스마트폰 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 할 때,
# 맨 처음 왼손 엄지손가락은 * 키패드에, 오른손 엄지 손가락은 # 키패드에 위치한다.
# 키패드를 누를 때 아래와 같은 규칙이 주어진다.

# 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
#    ㄴ 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

# 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
# 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 반환

# 예제
# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = 'left'
# result = 'LRLLRRLLLRR'

# 내가 푼 코드
# 우선, 키패드를 
# 1 2 3
# 4 5 6
# 7 8 9
# * 0 #    으로 보는 것이 아닌

# 1  2  3
# 4  5  6
# 7  8  9
# 10 11 12 로 두고 만약 numbers 배열에 0이 포함되어 있다면 0을 11으로 바꿔준다.

# 눌러야할 키패드에 키패드의 행의 수 3을 나누어 나머지가 1이라면 [1, 4, 7] 중 하나이므로 L을 answer에 추가한다.
# 눌러야 할 키패드에 3을 나눈 나머지가 0이면 [3, 6, 9] 중 하나이므로 answer에 R을 추가한다.
# 그 외의 경우 키패드가 [2, 5, 8, 0]인 경우인데 이때는 left와 right의 각각의 거리를 구하여 키패드를 누를 손을 정해준다.
# 왼손으로부터 거리가 더 가깝다면 왼손으로, 오른손이 더 가깝다면 오른손으로 키패드를 눌러야하므로 각각 상황에 맞게 answer에 저장해준다.

def solution(numbers, hand):
    answer = ''
    left, right = 10, 12
    
    for num in numbers:
        if num == 0:
            num = 11
            
        if num % 3 == 1:
            answer += 'L'
            left = num
            
        elif num % 3 == 0:
            answer += 'R'
            right = num
            
        else: 
            l_distance = abs(num-left)//3 + abs(num-left)%3
            r_distance = abs(num-right)//3 + abs(num-right)%3
            
            if l_distance > r_distance : 
                answer += 'R'
                right = num
                
            elif l_distance < r_distance:
                answer += 'L'
                left = num
                
            else:
                if hand == 'left':
                    answer += 'L'
                    left = num
                else:
                    answer += 'R'
                    right = num
    
    
    return answer


# 다른 사람 풀이 : 딕셔너리를 이용한 방법

def solution(numbers, hand):
    answer = ''

    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}

    left = dic['*']
    right = dic['#']
    
    for i in numbers:
        now = dic[i]

        if i in [1, 4, 7]:
            answer += 'L'
            left = now
            
        elif i in [3, 6, 9]:
            answer += 'R'
            right = now
            
        else:
            left_d = 0
            right_d = 0

            for a, b, c in zip(left, right, now):
                left_d += abs(a-c)
                right_d += abs(b-c)

            if left_d < right_d:
                answer += 'L'
                left = now

            elif left_d > right_d:
                answer += 'R'
                right = now

            else:
                if hand == 'left':
                    answer += 'L'
                    left = now

                else:
                    answer += 'R'
                    right = now
            
    return answer
