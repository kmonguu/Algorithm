// 조카는 아직 "aya", "ye", "woo", "ma" 네 가지 발음을 최대 한 번씩 사용해 조합한(이어 붙인) 발음밖에 하지 못한다.
// 문자열 배열 babbling이 매개변수로 주어질 때, 조카가 발음할 수 있는 단어의 수를 출력

// 예제
// ["aya", "yee", "u", "maa", "wyeoo"]-> 	1
// ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"] -> 	3


// 내가 푼 코드
// babbling 배열과 speak 배열을 각각 for문을 통해 순회하면서 
// 같은 문자가 있다면 ' ' 공백과 치환해준다.
// 만약, 조카가 발음을 할 수 있는 단어 조합이라면 해당 발음이 전부 공백으로 치환되었기 때문에
// trim()으로 공백을 제거해주고 해당 단어의 길이가 0이라면 모두 발음할 수 있는 단어로 만들어졌다는 의미이므로 answer에 +1 해준다.

function solution(babbling) {
    let answer = 0;
    let speak = ['aya', 'ye', 'woo', 'ma']
    let word = ''
    
    for (let i = 0; i < babbling.length; i++) {
        word = babbling[i].toString()
        
        for (let j = 0; j < speak.length; j++) {
            word = word.replaceAll(speak[j], ' ')
        }
        if (word.trim().length == 0) {
            answer = answer +1
        }
    }
    return answer
}
