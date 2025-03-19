class Solution {
public:
    vector<int> getSneakyNumbers(vector<int>& nums) {
        unordered_map<int, int> hashmap;

        for (int x : nums) {
            hashmap[x]++;
        }

        vector<int> result;

        for (const auto& pair : hashmap) {
            if (pair.second == 2) {
                result.push_back(pair.first);
            }
        }

        return result;
    }
};