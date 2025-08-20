/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function (matrix) {
  const m = Array.from({ length: matrix.length }, () => Array(matrix[0].length).fill(0));
  let res = 0;
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (i - 1 < 0 || j - 1 < 0) {
        res += matrix[i][j];
        m[i][j] = matrix[i][j];
      } else {
        if (matrix[i][j] === 1) {
          min = Math.min(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1]);
          res += min + 1;
          m[i][j] = min + 1;
        } else {
          m[i][j] = 0;
        }
      }
    }
  }
  return res;
};

let matrix = [
  [0, 1, 1, 1],
  [1, 1, 1, 1],
  [0, 1, 1, 1],
];

console.log(countSquares(matrix));
