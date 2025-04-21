class Solution {
public:
    bool areOccurrencesEqual(string s) {
        unordered_map<char, int> hashmap;
        set<int> res;

        for (char x : s) {
            hashmap[x]++;
        }

        for (const auto& [key, value] : hashmap) {
            res.insert(value);
        }

        return (res.size() == 1);
    }
};