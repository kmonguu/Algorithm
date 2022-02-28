// 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성되어 있다면 True, 아니면 False를 반환

// 내가 푼 코드
// 문자열에 'e'가 있다면 이를 숫자로 인식하여 true를 반환하는 문제를 해결하기 위해 문자열 s에 'e'가 있다면 다른 특수 문자로 치환시켜줌
// 해당 문자열이 숫자로 구성되어 있다면 true를 반환, 아니라면 false를 반환

function solution(s) {
    return (s.length == 4 || s.length == 6) && !isNaN(s.replace('e', '*'));
}
