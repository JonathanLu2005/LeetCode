class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int,int> hashmap;

        for (int x : nums) {
            hashmap[x]++;
        }

        for (const auto& pair : hashmap) {
            if (pair.second == 1) {
                return pair.first;
            }
        }

        return 0;
    }
};