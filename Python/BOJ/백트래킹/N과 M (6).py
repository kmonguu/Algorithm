# 자연수 N과 M이 주어졌을 때, 모두 다른 수 N개의 자연수 중에서 M개를 고른 수열을 반환
# 고른 수열은 오름차순이어야 하며 중복되는 수열을 여러 번 출력하면 안된다.

# 내가 푼 코드
# 수열이 오름차순이라는 말은 [2, 1], [1, 1]처럼 앞의 숫자가 뒤의 숫자보다 작거나 같으면 안된다는 것이다.
# 위의 경우를 방지하기 위해 start를 매개변수로 주어 재귀함수가 호출되었을 때, 현재 인덱스에 +1을 매개변수로 줌

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
answer = []

def n_and_m(start):
  if len(answer) == m:
    print(' '.join(map(str, answer)))
    return
  
  for idx in range(start, n):
    if arr[idx] not in answer:
      answer.append(arr[idx])
      n_and_m(idx+1)
      answer.pop()

n_and_m(0)
