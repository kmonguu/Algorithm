// 2016년 1월 1일이 금요일일 때, 2016년 a월 b일은 무슨 요일인지 반환
// 2016년은 윤년이다.

// 내가 푼 코드
// reduce 함수를 사용하여 입력된 a월 까지 일 수를 더한 값에 b일을 더해 일주일이 반복되는 7을 나누어 요일을 구함

function solution(a, b) {
    let month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    let week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    return week[((month.slice(0, a).reduce((acc, i) => (acc+i))) + b) % 7];
}
