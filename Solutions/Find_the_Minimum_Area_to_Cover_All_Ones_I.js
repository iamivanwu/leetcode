/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumArea = function (grid) {
  let t = grid.length;
  let b = 0;
  let l = grid[0].length;
  let r = 0;
  for (let i = 0; i < grid.length; i++) {
    for (let j = 0; j < grid[0].length; j++) {
      if (grid[i][j] === 1) {
        if (i <= t) {
          t = i;
        }
        if (i >= b) {
          b = i;
        }
        if (j <= l) {
          l = j;
        }
        if (j >= r) {
          r = j;
        }
      }
    }
  }
  return (b - t + 1) * (r - l + 1);
};
