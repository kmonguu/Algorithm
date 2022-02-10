# 자연수 N과 M이 주어졌을 때, 모두 다른 수 N개의 자연수 중에서 M개를 고른 수열을 반환
# 중복되는 수열을 여러 번 출력하면 안된다.

# 내가 푼 코드
# N개의 서로 다른 자연수를 arr배열에 오름차순으로 정렬한 후 저장한다.
# 만약, answer의 배열 길이가 m과 같다면 출력해주고, 아니라면 for문의 범위를 arr 배열의 인덱스로 하여 접근한다.
# 수열이 중복되는 것을 방지하기 위해 if문으로 조건을 걸어주고 재귀함수를 호출한다.

n, m = map(int, input().split())
arr = sorted(map(int, input().split()))
answer = []

def n_and_m():
  if len(answer) == m:
    print(' '.join(map(str, answer)))
    return 

  for idx in range(n):
    if arr[idx] not in answer:
      answer.append(arr[idx])
      n_and_m()
      answer.pop()

n_and_m()
