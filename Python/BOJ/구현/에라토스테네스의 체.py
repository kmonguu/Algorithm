# 에라토스테네스의 체는 n보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.
# n, k가 주어졌을 때, k 번째에 지워지는 수를 출력

# 내가 푼 코드
# 풀이
# 2 ~ n까지 배열을 만들어놓고, 이를 돌면서 True 값이 있다면 해당 값의 배수들을 모두 False로 만들어 소수가 아닌 수를 제거한다.
# 요소를 False로 바꿀 때마다 카운트를 하여 k와 카운트가 같아졌을 때의 값을 출력한다.

n, k = map(int, input().split())

arr = [True] * (n+1)
arr[0] = arr[1] = False

num = 0
for i in range(2, n+1):
  for j in range(i, n+1, i):
      arr[j] = False
      num += 1
      
      if num == k:
        print(j) 
        break
