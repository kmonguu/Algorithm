# 신규 유저가 입력한 아이디를 나타내는 new_id가 매개변수로 주어질 때, "네오"가 설계한 7단계의 처리 과정을 거친 후의 추천 아이디를 반환
# 7단계의 처리 단계는 다음과 같다.

# 예를 들어, new_id 값이 "...!@BaT#*..y.abcdefghijklm" 라면, 위 7단계를 거치고 나면 new_id는 아래와 같이 변경된다.

# 1단계 대문자 'B'와 'T'가 소문자 'b'와 't'로 바뀐다.
# "...!@BaT#*..y.abcdefghijklm" → "...!@bat#*..y.abcdefghijklm"

# 2단계 '!', '@', '#', '*' 문자가 제거되었습니다.
# "...!@bat#*..y.abcdefghijklm" → "...bat..y.abcdefghijklm"

# 3단계 '...'와 '..' 가 '.'로 바뀌었습니다.
# "...bat..y.abcdefghijklm" → ".bat.y.abcdefghijklm"

# 4단계 아이디의 처음에 위치한 '.'가 제거되었습니다.
# ".bat.y.abcdefghijklm" → "bat.y.abcdefghijklm"

# 5단계 아이디가 빈 문자열이 아니므로 변화가 없습니다.
# "bat.y.abcdefghijklm" → "bat.y.abcdefghijklm"

# 6단계 아이디의 길이가 16자 이상이므로, 처음 15자를 제외한 나머지 문자들이 제거되었습니다.
# "bat.y.abcdefghijklm" → "bat.y.abcdefghi"

# 7단계 아이디의 길이가 2자 이하가 아니므로 변화가 없습니다.
# "bat.y.abcdefghi" → "bat.y.abcdefghi"

# 결과적으로 신규 유저가 입력한 new_id가 "...!@BaT#*..y.abcdefghijklm"일 때, 네오의 프로그램이 추천하는 새로운 아이디는 "bat.y.abcdefghi"가 된다.

# 내가 푼 코드 
# 정규식을 이용하는 풀이
