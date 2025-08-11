class Solution {
public:
    int similarPairs(vector<string>& words) {
        // pair of similar strings = use same characters
        // convert each to set of characters
        // then store in hashmap
        // if 3, then 1-2, 1-3, 2-3
        // if 4 then 1-2, 1-3, 1-4, 2-3, 2-4, 3-4
        // if 2 then 1
        // if 1 then 0
        // so its n(n-1) / 2 ?

        map<set<char>, int> myMap;

        for (string word : words) {
            set<char> mySet;

            for (char c : word) {
                mySet.insert(c);
            }
            myMap[mySet]++;
        }

        int res = 0;

        for (const auto& [key, value] : myMap) {
            res += (value * (value-1) / 2);
        }

        return res;
    }
};