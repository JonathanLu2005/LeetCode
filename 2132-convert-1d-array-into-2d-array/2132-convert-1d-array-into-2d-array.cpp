class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        if (original.size() != m * n) {
            return {};
        }
        
        vector<vector<int>> result;
        vector<int> temp;

        int c = 0;

        for (int x : original) {
            temp.push_back(x);
            c++;

            if (c==n) {
                result.push_back(temp);
                temp = {};
                c=0;
            }
        }

        return result;
    }
};