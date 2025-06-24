class Solution {
public:
    string reversePrefix(string word, char ch) {
        // keep getting prefix until we hit ch, then we stop and reverse it
        // else same, first occurence

        bool first = false;
        string result;

        for (char c: word) {
            if (!(first) && (c == ch)) {
                result += c;
                first = true;
                reverse(result.begin(), result.end());
            } else {
                result += c;
            }
        }

        return result;
    }
};