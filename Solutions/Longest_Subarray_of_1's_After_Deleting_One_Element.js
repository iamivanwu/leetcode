/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function (nums) {
  let res = 0;
  let last = 0;
  let current = 0;
  let f = false;
  for (const num of nums) {
    if (num === 0) {
      f = true;
      last = current;
      current = 0;
    } else {
      current += 1;
    }
    res = Math.max(last + current, res);
  }
  return f ? res : res - 1;
};
