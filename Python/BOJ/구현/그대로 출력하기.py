# 입력받은 대로 출력하는 프로그램
# 입력은 최대 100줄로 이루어져 있고, 알파벳 소문자, 대문자, 공백, 숫자로만 이루어져 있다.


# 풀이
# 입력값이 몇 번 주어지는 지 모르지만 입력된 값이 그대로 출력되어야 한다.
# try, except 구문을 통해 입력값이 들어오면 그대로 출력하고, 입력값이 안들어온다면 break를 해준다.

# 코드
while True:
  try:
    print(int(input())
  except EOFerror:
    break
