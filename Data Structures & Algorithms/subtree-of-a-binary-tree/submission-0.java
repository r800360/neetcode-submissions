/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {  
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (p == null) {
            return false;
        } else if (q == null) {
            return false;
        }
        if (p.val != q.val) {
            return false;
        }

        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        if (isSameTree(root, subRoot)) {
            return true;
        }
        if (root.left == null && root.right == null) {
            return false;
        } else if (root.left == null) {
            return isSubtree(root.right, subRoot);
        } else if (root.right == null) {
            return isSubtree(root.left, subRoot);
        } else {
            return isSubtree(root.left, subRoot) || isSubtree(root.right, subRoot);
        }
        
    }
}
