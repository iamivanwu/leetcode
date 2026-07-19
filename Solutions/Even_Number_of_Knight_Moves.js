/**
 * @param {number[]} start
 * @param {number[]} target
 * @return {boolean}
 */
var canReach = function(start, target) {
    return !(Math.abs((start[0]+start[1] - target[0]-target[1]) % 2))
}