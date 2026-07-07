/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
  for (let i = 2; i < nums.length; i++) {
    if (nums[i] === nums[i - 1] && nums[i] === nums[i - 2]) {
      nums.splice(i, 1);
      i -= 1;
    }
  }
  return nums.length;
};

var a = [1, 1, 1, 2, 2, 3];
console.log(removeDuplicates(a), a);
