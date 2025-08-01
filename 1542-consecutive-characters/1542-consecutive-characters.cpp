class Solution {
public:
    int maxPower(string s) {
        int res = 1;
        int cur = 1;

        for (int i = 1; i < s.length(); i++) {
            if (s[i] == s[i-1]) {
                cur++;
            } else {
                res = max(res,cur);
                cur = 1;
            }
        }

        res = max(res,cur);

        return res;
    }
};