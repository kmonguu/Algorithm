// 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성되어 있다면 True, 아니면 False를 반환

// 내가 푼 코드
// s가 숫자인지 문자인지 확인하기 위해 isNaN 함수를 이용, 이때, 2e10과 같이 e도 숫자로 인식하기 때문에 다른 문자로 변환해줘야함
// 따라서 문자열 s에 'e'가 있다면 다른 특수 문자로 치환시켜줌
// 해당 문자열이 숫자로 구성되어 있다면 true를 반환, 아니라면 false를 반환

function solution(s) {
    return (s.length == 4 || s.length == 6) && !isNaN(s.replace('e', '*'));
}
