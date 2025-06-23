class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        // want indices that are same 0-0, 1-1, 2-2
        // then get length - 1, and whose indices add up to that
        int n = mat.size();
        int t = n-1;
        int m = mat[0].size();
        int res = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if ((i==j) || (i+j == t)) {
                    res += mat[i][j];
                }
            }
        }

        return res;

    }
};