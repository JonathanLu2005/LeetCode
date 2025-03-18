class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        int x = 0;

        for (const string& operation : operations) {
            if (operation.find("--") != string::npos) {
                x -= 1;
            } else {
                x += 1;
            }
        }

        return x;
    }
};