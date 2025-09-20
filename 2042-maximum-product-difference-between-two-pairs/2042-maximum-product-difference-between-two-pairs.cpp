class Solution {
public:
    int maxProductDifference(vector<int>& nums) {
        // just choose 2 max, 2 min, and do the magic
        int n = nums.size();

        sort(nums.begin(), nums.end());

        int s = nums[0] * nums[1];
        int l = nums[n-1] * nums[n-2];

        return l - s;
    }
};