class Solution {
public:
    int countKDifference(vector<int>& nums, int k) {
        // for loop, see if x - k exist in map
        // if so increment by how many of it exist
        unordered_map<int,int> map;
        int res = 0;

        for (int x : nums) {
            int key = x-k;
            if (map.find(key) != map.end()) {
                res += map[key];
            }

            key = x + k;
            if (map.find(key) != map.end()) {
                res += map[key];
            }            

            map[x]++;
        }

        return res;
    }
};