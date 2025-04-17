class Solution {
public:
    int sumOfGoodNumbers(vector<int>& nums, int k) {
        int res = 0;

        for (int i = 0; i < nums.size(); i++) {
            int val = nums[i];

            if (((i-k >= 0) && (nums[i-k] >= val)) || ((i+k < nums.size()) && (nums[i+k] >= val))) {
                continue;
            }
            res += val;
        }

        return res;
    }
};