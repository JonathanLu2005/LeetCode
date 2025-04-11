class Solution {
public:
    int thirdMax(vector<int>& nums) {
        set<int, greater<int>> numsSet(nums.begin(), nums.end());
        vector<int> result(numsSet.begin(), numsSet.end());

        if (result.size() >= 3) {
            return result[2];
        }
        return result[0];
    }
};