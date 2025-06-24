class MyHashMap {
private:
    map<int, int> hashmap;

public:
    MyHashMap() {
    }
    
    void put(int key, int value) {
        this->hashmap[key] = value;
    }
    
    int get(int key) {
        if (this->hashmap.find(key) != this->hashmap.end()) {
            return this->hashmap[key];
        }
        return -1;
    }
    
    void remove(int key) {
        this->hashmap.erase(key);
    }
};

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap* obj = new MyHashMap();
 * obj->put(key,value);
 * int param_2 = obj->get(key);
 * obj->remove(key);
 */