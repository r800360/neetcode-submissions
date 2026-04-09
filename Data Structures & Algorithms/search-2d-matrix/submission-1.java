class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        int n = matrix[0].length;
        int start = 0;
        int end = m*n - 1;
        while (start <= end) {
            int mid = start + (end - start)/2;
            // 0 -> [0][0], n-1 -> [0][n-1], m*n-1 -> [m-1][n-1]
            int curr = matrix[mid/n][mid%n];
            if (curr == target) {
                return true;
            } else if (curr < target) {
                start = mid + 1;
            } else {
                //curr > target
                end = mid - 1;
            }
        }

        return false;
    }
}
