class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        // number of rows = number of columns
        // number of columns = number of rows
        //int newCol = matrix.size();
        int newRow = matrix[0].size();

        vector<vector<int>> result(newRow);

        int row = 0;

        for (vector<int> array : matrix) {
            for (int x : array) {
                result[row].push_back(x);
                row++;
            }
            row = 0;
        }

        return result;
    }   
};