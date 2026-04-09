class Solution {
    public boolean isValid(String s) {
        Stack<Character> myStack = new Stack<Character>();
        int pointer = 0;
        while (pointer < s.length()) {
            char myChar = s.charAt(pointer);
            if ((myChar == '[') || (myChar == '{') || (myChar == '(')) {
                myStack.push(myChar);
            } else {
                if (myStack.empty()) {
                    return false;
                }

                char startChar = myStack.peek();
                if (((myChar == ']') && (startChar == '[') ) ||
                ((myChar == '}') && (startChar == '{') ) ||
                ((myChar == ')') && (startChar == '(') ) ) {
                    myStack.pop();
                } else {
                    return false;
                }

            }
            pointer++;
        }
        return myStack.empty();
    }
}
