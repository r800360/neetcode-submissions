class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> myStack = new Stack<Integer>();
        for (String token : tokens) {
            Character first = token.charAt(0);
            if (first == '+') {
                myStack.push(myStack.pop() + myStack.pop());
            } else if ((first == '-') && (token.length() == 1)) {
                myStack.push(-1 * myStack.pop() + myStack.pop());
            } else if (first == '*') {
                myStack.push(myStack.pop() * myStack.pop());
            } else if (first == '/') {
                int firstNum = myStack.pop();
                int secondNum = myStack.pop();

                myStack.push(secondNum / firstNum);
            } else {
                //token is an integer in range [-100, 100]
                int tokenInt = Integer.valueOf(token);
                myStack.push(tokenInt);
            }
            
        }
        int result = Integer.valueOf(myStack.pop());
        if (myStack.empty()) {
            return result;
        } else {
            return -1;
        }
    }
}
