class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int,int> hashmap;

        for (int num : nums) {
            hashmap[num]++;
        }

        for (const auto& [key, value] : hashmap) {
            if (value > (nums.size() / 2)) {
                return key;
            }
        }

        return 0;
    }
};