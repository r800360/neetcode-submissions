class MinStack {

    private ArrayList<Integer> stack;
    private ArrayList<Integer> minStack;

    public MinStack() {
        stack = new ArrayList<Integer>();
        minStack = new ArrayList<Integer>();
    }
    
    public void push(int val) {
        stack.add(val);
        if (minStack.size() == 0 || val <= minStack.get(minStack.size()-1)) {
            minStack.add(val);
        }
    }
    
    public void pop() {
        int poppedValue = stack.remove(stack.size()-1);
        if (poppedValue == minStack.get(minStack.size()-1)) {
            minStack.remove(minStack.size()-1);
        }
    }
    
    public int top() {
        return stack.get(stack.size()-1);
    }
    
    public int getMin() {
        return minStack.get(minStack.size()-1);
    }
}
