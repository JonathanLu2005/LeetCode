class Solution {
public:
    vector<int> findMissingAndRepeatedValues(vector<vector<int>>& grid) {
        // hashmap store count
        // set store number encounter
        // then do difference

        unordered_map<int, int> hashmap;
        unordered_set<int> set;
        int n = grid.size();
        vector<int> result;

        for (vector<int> array : grid) {
            for (int x : array) {
                hashmap[x]++;
                set.insert(x);

                if (hashmap[x] == 2) {
                    result.push_back(x);
                }
            }
        }

        for (int i = 1; i <= pow(n,2); i++) {
            if (set.find(i) == set.end()) {
                result.push_back(i);
                break;
            }
        }

        return result;
    }
};