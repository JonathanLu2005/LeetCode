class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        unordered_map<int, int> map;
        
        vector<int> numsCopy = nums;
        sort(numsCopy.begin(), numsCopy.end());

        for (int i = 0; i < numsCopy.size(); i++) {
            int key = numsCopy[i];

            if (map.find(key) == map.end()) {
                map[key] = i;
            }
        }

        for (int i = 0; i < nums.size(); i++) {
            int key = nums[i];

            nums[i] = map[key];
        }

        return nums;


    }
};