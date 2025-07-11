class Solution {
public:
    string replaceDigits(string s) {
        string result = "";
        int current = 0;

        for (char c : s) {
            if (isdigit(c)) {
                current += c - '0';

                if (current > 122) {
                    current -= 26;
                }

                result += (char)current;
                current = 0;
            } else {
                current = (int)c;
                result += c;
            }
        }
        return result;
    }
};