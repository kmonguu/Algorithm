// 어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 한다.
// 문자열 s와 거리 n이 매개 변수로 주어질 때, s를 n만큼 민 암호문을 반환

// 내가 푼 코드 (인터넷 참고)
// 문자열 s를 split("")으로 배열로 만들어준 뒤 map을 이용
// answer에 대문자로 변화시킨 알파벳을 아스키 코드로 변환한 뒤, n을 더했을 때 90이 넘는다면 'Z'를 넘어가는 값이므로
// 알파벳을 순환하여 처음 'A'로 돌아가기 위해 26을 뺸 후 다시 문자열로 바꿈
// 그렇지 않을 경우 answer를 아스키 코드로 변환한 값에 n만 더하여 문자열로 바꾸어 반환

// 자바스크립트에서 아스키 코드로 변환하는 charCodeAt()과 문자열로 다시 변환하는 String.fromCharCode()를 알게 됨

function solution(s, n){
    return s.split("").map(answer => {
        if (answer === " ") return answer;
        return answer.toUpperCase().charCodeAt() + n > 90
        ? String.fromCharCode(answer.charCodeAt() + n - 26)
        : String.fromCharCode(answer.charCodeAt() + n)
    }).join("");
}
