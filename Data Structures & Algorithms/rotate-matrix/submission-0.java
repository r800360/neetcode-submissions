class Solution {
    public void rotate(int[][] matrix) {
        // Idea is rotation is two reflections - diagonal and vertical
        int m = matrix.length;
        int temp = 0;
        // Main diagonal reflection
        for (int i = 0; i < matrix.length; i++) {
            for (int j = i+1; j < matrix.length; j++) {
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i];
                matrix[j][i] = temp;
            }
        }
        // Vertical reflection
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix.length/2; j++) {
                temp = matrix[i][j];
                matrix[i][j] = matrix[i][m - j - 1];
                matrix[i][m - j - 1] = temp;
            }
        }
    }
}
