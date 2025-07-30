class Solution {
public:
    string truncateSentence(string s, int k) {
        // contain first k words
        // so when hit 4th space
        int count = 0;
        string res = "";

        if (k==0) {
            return res;
        }

        for (char c : s) {
            if (c == ' ') {
                count++;
            }

            if (count==k) {
                return res;
            }

            res += c;
        }
        return res;
    }
};