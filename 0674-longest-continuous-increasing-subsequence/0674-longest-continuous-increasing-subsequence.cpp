class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int n = nums.size();
        int cur = 1;
        int res = 1;

        for (int i = 1; i < n; i ++) {
            if (nums[i] > nums[i-1]) {
                cur += 1;
            } else {
                res = max(res,cur);
                cur = 1;
            }
        }
        res = max(res,cur);
        return res;
    }
};