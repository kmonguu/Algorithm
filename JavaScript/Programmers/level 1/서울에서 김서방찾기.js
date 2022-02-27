// 문자열 배열 seoul이 매개변수로 주어졌을 때, 'Kim'의 위치를 찾아 반환

// 내가 푼 코드
// 표현식을 ${…}로 감싸고 이를 백틱으로 감싼 문자열 중간에 넣어 'Kim'씨가 몇 번째 인덱스에 있는지 반환

function solution(seoul) {
    return `김서방은 ${seoul.indexOf("Kim")}에 있다`
}
