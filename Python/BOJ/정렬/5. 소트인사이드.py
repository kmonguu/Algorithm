# 수가 주어지면 그 수의 각 자리수를 내림차순으로 정렬하여 출력

N = input()

N_list = [] 
for i in N:
  N_list.append(i)                    # 입력받은 N 변수의 각 자리수를 N_list 배열에 저장
  N_list.sort(reverse=True)           # N_list 배열에 담긴 수를 reverse=True를 통해 내림차순으로 정렬

print("".join(map(str, N_list)))      # 배열에 든 내림차순으로 정렬된 수를 join을 통해 공백없이 출력




# 다른 방법

print(*sorted(input(), reverse=True), sep='')  # *을 통해 배열에 담긴 수를 꺼낸 다음 sep을 통해 공백없이 수를 출력
