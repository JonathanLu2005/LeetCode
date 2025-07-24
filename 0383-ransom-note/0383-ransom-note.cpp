class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        set<char> keys;
        map<char,int> ransom;
        map<char,int> capacity;

        for (char c : ransomNote) {
            keys.insert(c);
            ransom[c]++;
        }

        for (char c : magazine) {
            capacity[c]++;
        }

        for (char c : keys) {
            if (ransom[c] > capacity[c]) {
                return false;
            }
        }

        return true;
    }
};