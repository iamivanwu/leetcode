/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var countDominantNodes = function (root) {
    let res = 0;
    const f = (tree) => {
        if (!tree) {
            return 0;
        }

        const l = f(tree.left);
        const r = f(tree.right);

        const m = Math.max(tree.val, l, r);
        if (tree.val >= m) {
            res += 1;
        }
        return m;
    };
    f(root);
    return res;
};