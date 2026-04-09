class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        // index stack
        Stack<Integer> myStack = new Stack<Integer>();
        int n = temperatures.length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            while (!myStack.empty() && temperatures[i] > temperatures[myStack.peek()]) {
                int index = myStack.pop();
                result[index] = i - index;
            }

            myStack.push(i);
        }

        return result;
    }
}
