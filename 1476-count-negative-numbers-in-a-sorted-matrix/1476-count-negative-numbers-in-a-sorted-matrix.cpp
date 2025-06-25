class Solution {
public:
    int countNegatives(vector<vector<int>>& grid) {
        int r = grid.size();
        int c = grid[0].size();
        int res = 0;

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                int v = grid[i][j];

                if (v < 0) {
                    res++;
                }
            }
        }

        return res;
    }
};