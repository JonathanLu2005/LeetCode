class Solution {
public:
    char repeatedCharacter(string s) {
        unordered_map<char,int> hashmap;

        for (char c : s) {
            if (hashmap.contains(c)) {
                return c;
            } else {
                hashmap[c] = 1;
            }
        }

        return 'a';
    }
};