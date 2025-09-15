class Solution {
public:
    int maximizeSum(vector<int>& nums, int k) {
        // leigt just get the max number
        // multiply it by k
        // then add something
        int v = *max_element(nums.begin(), nums.end());
        return v * k + (k * (k - 1)) / 2;
    }
};