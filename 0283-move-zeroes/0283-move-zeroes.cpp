class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int count = 0;

        for (int x : nums) {
            if (x == 0) {
                count++;
            }
        }

        auto result = remove(nums.begin(), nums.end(), 0);

        nums.erase(result, nums.end());

        while (count > 0) {
            nums.push_back(0);
            count--;
        }
    }
};