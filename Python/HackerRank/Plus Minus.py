# 범위가 -100 <= arr[i] <= 100 인 요소가 담긴 배열 arr이 주어질 때, 
# arr배열의 양의 정수, 음의 정수, 0의 비율을 반환

# 내가 푼 코드
# 차례대로 양의 정수의 개수, 음의 정수의 개수, 0의 개수를 저장하는 배열 cnt를 0으로 초기화
# arr 배열을 순회하면서 각각의 개수를 cnt에 저장
# 비율을 반환해야 하므로 arr 배열의 길이 n을 나눈 값을 소수점 6자리까지 나타내어 반환

def plusMinus(arr):
    # Write your code here
    cnt = [0, 0, 0]
    for num in arr:
        if num > 0:
            cnt[0] += 1
        elif num < 0:
            cnt[1] += 1
        else:
            cnt[2] += 1
    
    for i in cnt:
        print(format(i/n, ".6f"))
