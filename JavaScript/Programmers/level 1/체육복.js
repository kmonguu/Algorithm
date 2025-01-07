function solution(n, lost, reserve) {
  let student = new Array(n).fill(1);
  reserve.sort((a, b) => a - b).forEach((index) => (student[index - 1] += 1));
  lost.sort((a, b) => a - b).forEach((index) => (student[index - 1] -= 1));

  for (let i = 0; i < student.length; i++) {
    if (student[i] === 2) {
      if (i - 1 >= 0 && !student[i - 1]) {
        student[i] -= 1;
        student[i - 1] += 1;
      } else if (i + 1 < student.length && !student[i + 1]) {
        student[i] -= 1;
        student[i + 1] += 1;
      }
    }
  }
  let result = 0;
  for (let i = 0; i < student.length; i++) {
    if (student[i]) result += 1;
  }
  return result;
}
