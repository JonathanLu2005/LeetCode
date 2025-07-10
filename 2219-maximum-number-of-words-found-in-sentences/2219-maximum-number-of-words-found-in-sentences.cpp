class Solution {
public:
    int mostWordsFound(vector<string>& sentences) {
        // just count number of spaces, number of spaces then + 1 more, and store if its max
        int res = 0;
        for (string sentence : sentences) {
            int count = 0;
            for (char c : sentence) {
                if (c == ' ') {
                    count++;
                }
            }

            if (count > res) {
                res = count;
            }
        }

        return ++res;
    }
};