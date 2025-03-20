class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        int result = 0;
        set<char> allowedSet(allowed.begin(), allowed.end());

        for (string word : words) {
            bool consistent = true;

            for (char c : word) {
                if (allowedSet.find(c) == allowedSet.end()) {
                    consistent = false;
                    break;
                }
            }

            if (consistent) {
                result++;
            }
        }
        return result;
    }
};