class MyHashSet {
private:
    unordered_set<int> hashset;

public:
    MyHashSet() {
        
    }
    
    void add(int key) {
        this->hashset.insert(key);
    }
    
    void remove(int key) {
        this->hashset.erase(key);
    }
    
    bool contains(int key) {
        return hashset.find(key) != hashset.end();
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */