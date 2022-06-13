# 2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.

# 내가 푼 코드
# n의 크기가 증가함에 따라 필요한 타일의 수는 파보나치 수열의 규칙을 따르는 것을 알 수 있다.

num = int(input())
answer = [0] * (num+1)

answer[0] = answer[1] = 1

for idx in range(2, num+1):
  answer[idx] = (answer[idx-1] + answer[idx-2]) % 10007

print(answer[num])
