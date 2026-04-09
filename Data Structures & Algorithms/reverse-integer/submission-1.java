class Solution {
    public int reverse(int x) {
        if (x == 0) {
            return 0;
        }
        boolean negativeFlag = false;
        if (x < 0) {
            negativeFlag = true;
            x = -x;
        }

        int result = 0;
        while (x != 0) {
            int digit = x % 10;

            if (result > (Integer.MAX_VALUE - digit) / 10) {
                return 0;
            }

            result = result * 10 + digit;
            x /= 10;
        }
        if (negativeFlag) {
            result *= -1;
        }
        return result;
    }
}
