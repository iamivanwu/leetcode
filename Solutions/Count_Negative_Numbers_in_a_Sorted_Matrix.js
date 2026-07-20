/**
 * @param {number[][]} grid
 * @return {number}
 */
var countNegatives = function (grid) {
  const bs = (arr) => {
    let l = 0;
    let r = arr.length - 1;
    let c = r + 1;
    while (l <= r) {
      let mid = Math.floor((l + r) / 2);
      if (arr[mid] >= 0) {
        l = mid + 1;
      } else {
        c = mid;
        r = mid - 1;
      }
    }
    return arr.length - 1 - (c - 1);
  };
  let s = 0;
  for (const g of grid) {
    s += bs(g);
  }
  return s;
};
