class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();

        for (int x = 0; x <= n; x++) {
            if (find(nums.begin(), nums.end(), x) == nums.end()) {
                return x;
            }
        }

        return n + 1;
    }
};