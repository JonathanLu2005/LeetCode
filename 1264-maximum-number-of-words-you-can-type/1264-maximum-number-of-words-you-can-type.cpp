class Solution {
public:
    int canBeTypedWords(string text, string brokenLetters) {
        set<char> myset;
        int res = 0;
        int cnt = 0;

        for (char c : brokenLetters) {
            myset.insert(c);
        }

        for (char c : text) {
            if (c == ' ') {
                if (cnt == 0) {
                    res++;
                }
                cnt = 0;
            } else {
                if (myset.find(c) != myset.end()) {
                    cnt++;
                }
            }
        }

        if (cnt == 0) {
            res++;
        }

        return res;
    }
};