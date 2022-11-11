# 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 반환

# 예제
# my_str                n     result
# "abc1Addfggg4556b"	6	  ["abc1Ad", "dfggg4", "556b"]
# "abcdef123"	        3	  ["abc", "def", "123"]

# 내가 푼 코드
def solution(my_str, n):
    return ([my_str[i:i+n] for i in range(0,len(my_str),n)])   
