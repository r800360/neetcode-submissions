class Solution {
    public int missingNumber(int[] nums) {
        // int result = 0;
        // for (int i = 0; i <= nums.length; i++) {
        //     result ^= i;
        // }
        // for (int num : nums) {
        //     result ^= num;
        // }
        // return result;
        int n = nums.length;
        int sum = 0;
        for (int num : nums) {
            sum += num;
        }
        return ((n*(n+1))/2-sum);
    }
}
