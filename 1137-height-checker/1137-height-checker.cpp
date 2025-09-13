class Solution {
public:
    int heightChecker(vector<int>& heights) {
        vector<int> copy = heights;
        sort(copy.begin(), copy.end());
        int result = 0;

        int n = heights.size();

        for (int i = 0; i < n; i++) {
            if (heights[i] != copy[i]) {
                result++;
            }
        }

        return result;
    }
};