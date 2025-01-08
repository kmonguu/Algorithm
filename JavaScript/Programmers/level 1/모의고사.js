function solution(answers) {
  const first = [1, 2, 3, 4, 5];
  const second = [2, 1, 2, 3, 2, 4, 2, 5];
  const third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
  const students = [
    repeatArrayToLength(first, answers.length),
    repeatArrayToLength(second, answers.length),
    repeatArrayToLength(third, answers.length),
  ];

  let result = [0, 0, 0];
  for (let i in students) {
    answers.forEach((answer, index) => {
      if (students[i][index] === answer) {
        result[i] += 1;
      }
    });
  }
  const max = Math.max(...result);
  const maxIndices = result
    .map((num, idx) => (num === max ? idx + 1 : -1))
    .filter((idx) => idx !== -1);
  return maxIndices;
}
function repeatArrayToLength(arr, length) {
  const repeated = [];
  while (repeated.length < length) {
    repeated.push(...arr);
  }
  return repeated.slice(0, length);
}
