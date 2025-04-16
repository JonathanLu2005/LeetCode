class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        // just do count and select whichever one has been appeared n times
        unordered_map<int, int> map;
        int n = 0;

        for (const auto& edge : edges) {
            map[edge[0]]++;
            map[edge[1]]++;
            n++;
        }

        for (const auto& [key, value] : map) {
            if (value == n) {
                return key;
            }
        }

        return 0;
    }
};