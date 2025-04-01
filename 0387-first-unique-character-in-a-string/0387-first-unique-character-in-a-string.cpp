class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char,int> hashmap;

        for (char c : s) {
            hashmap[c]++;
        }

        int index = 0;

        for (char c : s) {
            if (hashmap[c] == 1) {
                return index;
            }
            index++;
        }
        return -1;
    }
};