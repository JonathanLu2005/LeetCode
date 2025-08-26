class Solution {
public:
    int alternateDigitSum(int n) {
        bool add = true;
        int res = 0;
        string num = to_string(n);

        for (char c : num) {
            if (add) {
                res += c - '0';
                add = false;
            } else {
                res -= c - '0';
                add = true;
            }
        }

        return res;
    }
};