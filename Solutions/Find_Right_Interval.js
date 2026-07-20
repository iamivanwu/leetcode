/**
 * @param {number[][]} intervals
 * @return {number[]}
 */
var findRightInterval = function (intervals) {
  const arr = intervals.map((v, i) => [v[0], i]).sort((a, b) => a[0] - b[0]);
  const bs = (end) => {
    let l = 0;
    let r = arr.length - 1;
    let index = -1;
    while (l <= r) {
      let mid = Math.floor((l + r) / 2);
      if (arr[mid][0] < end) {
        l = mid + 1;
      } else {
        index = arr[mid][1];
        r = mid - 1;
      }
    }
    return index;
  };
  const res = [];
  for (const interval of intervals) {
    res.push(bs(interval[1]));
  }
  return res;
};
