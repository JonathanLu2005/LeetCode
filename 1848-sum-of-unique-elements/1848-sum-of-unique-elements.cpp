class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        unordered_map<int,int> hashmap;

        for (int num : nums) {
            if (hashmap.contains(num)) {
                hashmap[num] += 1;
            } else {
                hashmap[num] = 1;
            }
        }

        int res = 0;

        for (const auto& [key,value] : hashmap) {
            if (value == 1) {
                res += key;
            }
        }

        return res;
    }
};