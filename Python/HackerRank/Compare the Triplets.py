# Alice와 Bob의 점수표가 매개변수로 주어졌을 때, 둘의 점수를 비교하여 몇 대 몇의 스코어인지를 반환

# 예제
# Alice = [1, 2, 3], Bob = [3, 2, 1]
# 인덱스 별로 점수를 비교했을 때 스코어 현황은 1 대 1이 된다.

# 내가 푼 코드
# 인덱스 별로 점수를 비교하기 위해 zip으로 묶어주었다.
# [a점수, b점수]로 묶여 있는 점수를 서로 비교하여 score에 점수를 올려주었다.

def compareTriplets(a, b):
    # Write your code here
    score = [0, 0]
    for i in zip(a, b):
        if i[0] > i[1]:
            score[0] += 1
            
        elif i[0] < i[1]:
            score[1] += 1
    return score
            
