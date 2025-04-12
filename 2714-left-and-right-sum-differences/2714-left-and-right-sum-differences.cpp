class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        // left is 0 then 0 to n - 1
        // right is 0 then n to 1
        int n = nums.size();
        vector<int> left(n,0);
        vector<int> right(n,0);
        vector<int> result(n);

        for (int i = 1; i < n; i++) {
            left[i] = left[i-1] + nums[i-1];
        }
        for (int i = n - 2; i >= 0; i--) {
            right[i] = right[i+1] + nums[i+1];
        }
        for (int i = 0; i < n; i++) {
            int val = left[i] - right[i];
            result[i] = abs(val);
        }
        return result;
    }
};