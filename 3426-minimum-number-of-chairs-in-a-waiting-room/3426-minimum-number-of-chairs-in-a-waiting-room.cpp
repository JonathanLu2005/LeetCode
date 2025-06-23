class Solution {
public:
    int minimumChairs(string s) {
        // if theres L, we record number of E's we've as needed, then continue
        int res = 0;
        int cur = 0;

        for (char c : s) {
            if (c=='E') {
                cur++;
            } else {
                res = max(res,cur);
                cur--;
            }
        }
        res = max(res,cur);
        return res;
    }
};