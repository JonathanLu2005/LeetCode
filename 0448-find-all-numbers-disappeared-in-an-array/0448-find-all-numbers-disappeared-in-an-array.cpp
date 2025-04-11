class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> result;
        int n = nums.size();
        set<int> numsSet(nums.begin(), nums.end());

        for (int x = 1; x <= n; x++) {
            if (numsSet.find(x) == numsSet.end()) {
                result.push_back(x);
            }
        }

        return result;
    }
};