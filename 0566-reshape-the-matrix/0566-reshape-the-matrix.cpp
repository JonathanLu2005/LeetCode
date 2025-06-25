class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        // r are rows, c are columns
        // if legal return new shape, else return original
        int i = mat.size();
        int j = mat[0].size();

        if (i*j != r*c) {
            return mat;
        }

        vector<vector<int>> result;
        vector<int> temp;
        int count = 0;

        for (int x = 0; x < i; x++) {
            for (int y = 0; y < j; y++) {
                int v = mat[x][y];
                temp.push_back(v);
                count++;

                if (count==c) {
                    result.push_back(temp);
                    temp = {};
                    count = 0;
                }
            }
        }

        return result;
    }
};