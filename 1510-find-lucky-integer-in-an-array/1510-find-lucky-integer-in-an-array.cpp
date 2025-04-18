class Solution {
public:
    int findLucky(vector<int>& arr) {
        // lucky if frequency equivalanet to its value

        unordered_map<int,int> map;

        for (int x : arr) {
            map[x]++;
        }

        int res = -1;

        for (const auto& [key,value] : map) {
            if (key == value) {
                res = max(key, res);
            }
        }

        return res;
    }
};