// 영어 대소문자로 이루어진 문자열 my_string이 매개변수로 주어질 때, my_string을 모두 소문자로 바꾸고 알파벳 순서대로 정렬한 문자열을 반환

// 예제
"Bcad"   -> "abcd"
"heLLo"  -> "ehllo"
"Python" -> "hnopty"

// 내가 푼 코드
// 1. 문자열 속 대문자를 소문자로 변환
// 2. 단어 속 알파벳을 하나씩 분리 ex) python -> [ 'p', 'y', 't', 'h', 'o', 'n' ]
// 2. 소문자 문자열을 알파벳 순서로 정렬
// 3. 배열로 저장된 정렬된 알파벳을 문자열로 출력

function solution(my_string) {
    return my_string.toLowerCase().split('').sort().join('');
}
