class MyQueue {
private:
    vector<int> queue;

public:
    MyQueue() {
        this->queue = {};
    }
    
    void push(int x) {
        this->queue.push_back(x);
    }
    
    int pop() {
        int value = this->queue[0];
        this->queue.erase(this->queue.begin());
        return value;
    }
    
    int peek() {
        return (this->queue[0]);
    }
    
    bool empty() {
        return (this->queue.size() == 0);
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */