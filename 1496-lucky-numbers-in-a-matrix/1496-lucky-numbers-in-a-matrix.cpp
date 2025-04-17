class Solution {
public:
    vector<int> luckyNumbers(vector<vector<int>>& matrix) {
        int row = matrix.size();
        int col = matrix[0].size();

        vector<int> minRow(row, 1000000);
        vector<int> maxColumn(col, 0);

        for (int r = 0; r < row; r++) {
            for (int c = 0; c < col; c++) {
                int val = matrix[r][c];

                if (minRow[r] > val) {
                    minRow[r] = val;
                }

                if (maxColumn[c] < val) {
                    maxColumn[c] = val;
                }
            }
        }

        set<int> rowSet(minRow.begin(), minRow.end());
        set<int> colSet(maxColumn.begin(), maxColumn.end());

        vector<int> res;
        for (int x : rowSet) {
            if (colSet.find(x) != colSet.end()) {
                res.push_back(x);
            }
        }

        return res;
    }
};