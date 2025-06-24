class Solution {
public:
    string removeOuterParentheses(string s) {
        // when open = close brackets, then we stop, get rid of first and last index
        // then add it to result
        // and empty it
        string result;
        string current;
        int open = 0;
        int closed = 0;

        for (char c : s) {
            if (c == '(') {
                open++;
            } else {
                closed++;
            }

            if (open==closed) {
                current.erase(0,1);
                result += current;
                open = 0;
                closed = 0;
                current = "";
            } else {
                current += c;
            }
        }

        return result;
    }
};