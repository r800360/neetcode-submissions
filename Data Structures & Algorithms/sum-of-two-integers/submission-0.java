class Solution {
    public int getSum(int a, int b) {
        // XOR gives sum without carry
        // AND + shift gives carry 

        //inner loop logic
        int sum = 0;
        int carry = 0;
        
        while (b != 0) {
            sum = a ^ b;
            carry = (a & b) << 1;
            a = sum;
            b = carry;
        }
        
        return a;
    }
}
