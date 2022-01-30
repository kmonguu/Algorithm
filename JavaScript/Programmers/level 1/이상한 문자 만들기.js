// 문자열 s가 하나 이상의 단어로 구성되어 있을 때, 각 단어는 하나 이상의 공백문자로 구분되어 있다.
// 각 단어의 짝수번째 알파벳은 대문자, 홀수번째 알파벳은 소문자로 바꾼 문자열을 반환

// 내가 푼 코드

function solution(s) {
    let arr = s.split(" ");
    
    let answer = [];
    for (let i of arr){
        let word = ''
        for (let j = 0; j < i.length; j++){
            if (j % 2)
                word += i[j].toLowerCase();
            else
                word += i[j].toUpperCase();
        }
        answer.push(word)
    }
    return answer.join(' ');
}
