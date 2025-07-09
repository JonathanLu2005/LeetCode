class Solution {
public:
    bool digitCount(string num) {
        // get count of each
        // e.g 1 appears twice, 2 appears once, 0 appears once
        // then go through each index compared to string
        // so index 0, 0 appear once, 1 appear twice, 3 appear 0 times

        map<char,int> hashmap;

        for (char c : num) {
            hashmap[c]++;
        }

        int n = num.size();

        for (int i = 0; i < n; i++) {
            char amount = num[i];
            char key = '0' + i;
            char val = '0';

            if (hashmap.count(key)) {
                val = '0' + hashmap[key];
            }

            if (amount != val) {
                return false;
            }
        }

        return true;
    }
};