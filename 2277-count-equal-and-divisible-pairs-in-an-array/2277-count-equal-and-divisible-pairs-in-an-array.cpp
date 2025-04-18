class Solution {
public:
    int countPairs(vector<int>& nums, int k) {
        // given indices from 0 to n find which ones multiply to be divisible by whatever
        // then check if those actually works

        int res = 0;

        for (int i = 0; i < nums.size(); i++) {
            int iVal = nums[i];

            for (int j = i+1; j < nums.size(); j++) {
                int jVal = nums[j];

                if ((iVal == jVal) && (i * j % k == 0)) {
                    res++;
                }
            }
        }

        return res;
    }
};