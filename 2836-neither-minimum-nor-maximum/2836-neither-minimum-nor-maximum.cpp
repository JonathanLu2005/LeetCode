class Solution {
public:
    int findNonMinOrMax(vector<int>& nums) {
        set<int> numsSet(nums.begin(), nums.end());
        vector<int> result(numsSet.begin(), numsSet.end());

        if (result.size() <= 2) {
            return -1;
        }
        return result[1];
    }
};