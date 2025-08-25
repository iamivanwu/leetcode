/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findDiagonalOrder = function (mat) {
  let w = mat[0].length;
  let h = mat.length;
  let direction = 1;
  const res = [];
  let i = 0;
  let j = 0;
  while (i < h && j < w) {
    res.push(mat[i][j]);
    if (direction === 1) {
      if (i - 1 >= 0 && j + 1 < w) {
        i -= 1;
        j += 1;
      } else if (j + 1 < w) {
        j += 1;
        direction *= -1;
      } else {
        i += 1;
        direction *= -1;
      }
    } else {
      if (i + 1 < h && j - 1 >= 0) {
        i += 1;
        j -= 1;
      } else if (i + 1 < h) {
        i += 1;
        direction *= -1;
      } else {
        j += 1;
        direction *= -1;
      }
    }
  }
  return res;
};
