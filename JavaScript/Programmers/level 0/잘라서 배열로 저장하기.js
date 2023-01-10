// 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 반환

// 예제
// my_str               n     result
// "abc1Addfggg4556b"   6     ["abc1Ad", "dfggg4", "556b"]
// "abcdef123"          3     ["abc", "def", "123"]

// 내가 푼 코드
// 간단히 answer 배열에 push할 때, my_str[i:i+n]하면 될 줄 알았는데..
// 자바스크립트엔 배열 슬라이스를 slice()로 할 수 있는 걸 알게 됨

function solution(my_str, n) {
    var answer = [];
    for(let i = 0; i < my_str.length; i+=n) {
        answer.push(my_str.slice(i, i+n));
    }
    return answer;
}
