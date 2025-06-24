class MyStack {
private:
    vector<int> stack;

public:
    MyStack() {
        this->stack = {};
    }
    
    void push(int x) {
        this->stack.push_back(x);
    }
    
    int pop() {
        int value = this->stack.back();
        this->stack.pop_back();
        return value;
    }
    
    int top() {
        return this->stack.back();
    }
    
    bool empty() {
        return (this->stack.size() == 0);
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */